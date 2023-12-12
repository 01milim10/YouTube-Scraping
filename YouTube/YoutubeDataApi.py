##Importing libraries
import googleapiclient.discovery ##Library that helps us to use youtube data api v3
import pprint, json, time ##pretty print in the console; json file handler; 
import pandas as pd ##manipulate and save the data in desire file format

##Credentials required to authorize with youtube data api
api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBighmBrEqkN4wkPGIhv_9zC9eQm1pf7nc" ##Api key from youtube developer console
video_id = "TATSAHJKRd8" ##id of the video to scrape comments from 

youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY) ##create variable that helps us to access youtube data api endpoints

months = ['Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec'] ##Array of Month Names

##The main function where the code starts running
def main():
    ##Create a request to send to the youtube data api
    request = youtube.commentThreads().list(
        part="snippet, replies",
        videoId=video_id,
        maxResults=100)
        
    response = request.execute() ##Execute the request and save the response in response variable
    
    ##create a document named results-raw.json and open in write mode with utf-8 character encoding
    file = open('results-raw.json', 'w', encoding='utf-8')
    file.write(json.dumps(response, ensure_ascii=False, indent=4)) ##write the response as a json string in results-raw.json
    
    all_comments = response.get('items') ##Get items array from the response variable and store in all_comments variable
    
    has_next_page = 'nextPageToken' in response ##check if nextPageToken is in response. If yes has_next_page is true
    next_page_token = response.get('nextPageToken') ##Get nextPageToken from the response and save it in next_page_token
    
    ##Run if block if next_page_token is true
    if has_next_page is True:
        ##Call external method get_all_comments with video_id, next_page_token, max_results, has_next_page parameters. Retrieved comments are store in next_page_comments variable
        next_page_comments = get_all_comments(video_id=video_id,next_page_token=next_page_token, max_results=100, has_next_page=has_next_page)
        all_comments.extend(next_page_comments) ##Add next_page_comments to our all_comments variables
        scrape_comments(all_comments) ##Scrape all the comments from the first page using external methon=d scrape_comments
        
    else:
        scrape_comments(all_comments) ##Scrape all the comments from the first page using external methon=d scrape_comments

##Defination of get_all_comments method. video_id, max_results, next_page_token, has_next_page are the parameter required for this method        
def get_all_comments(video_id, max_results,next_page_token, has_next_page):
    comments = [] ##Initialize empty variable named comments
    while has_next_page:
        ##Create a new request to get the comments from the next page
        request = youtube.commentThreads().list(
        part="snippet, replies",
        videoId=video_id,
        maxResults=max_results,
        pageToken=next_page_token)
        
        response = request.execute() ##Execute the request and save the response on the response variable
        items = response.get('items') ##Get items array from the response and store in items variable
        comments.extend(items) ##Add the retrieved items to the comments variable
        
        next_page_token = response.get('nextPageToken') ##Check if nextPageToken is in response. If yes has_next_page is true
        has_next_page = 'nextPageToken' in response ##Get nextPageToken from the response and save it in next_page_token
    return comments ##Return all comments retrieved from the next pages

##Defination of get_comment_replies. It retrieves the replies for comments if it has any. parent_video_id is the only parameter required for this method    
def get_comment_replies(parent_video_id):
    replies = [] ##Initialize new empty variable named replies to store replies
    ##Create a youtube request to get replies and save it in response variable
    response = youtube.comments().list(
        part='snippet',
        maxResults= 100,
        parentId = parent_video_id,        
    ).execute()
    replies.extend(response.get('items'))  ##Get items array from the response and store it in response variable  
    has_next_page = 'nextPageToken' in response ##check if nextPageToken is in response. If yes has_next_page is true
    next_page_token = response.get('nextPageToken') ##Get nextPageToken from the response and save it in next_page_token
    
    ##Run this code block if has_next_page is true
    if has_next_page is True:
        ##Run this while loop until we fing has_next_page in the response
        while has_next_page:
            ##Create a request to get replies that are on next page
            request = youtube.comments().list(
            part="snippet",
            parentId = parent_video_id,
            maxResults=100,
            pageToken=next_page_token)
            
            response = request.execute() ##Execute the request and store the response in response variable
            items = response.get('items') ##Get the items array from the response and store it in items variable
            replies.extend(items) ##Add the items to the replies variable
            
            next_page_token = response.get('nextPageToken') ##check if nextPageToken is in response. If yes has_next_page is true
            has_next_page = 'nextPageToken' in response ##Get nextPageToken from the response and save it in next_page_token
        return replies    ##Return all the comments of replies collected 
    else:
        return replies    ##Return all the replies collected

##Function defination of scrape_comments with items as only parameter
def scrape_comments(items): 
    comments = [] ##Initialize new empty variable named comments to store comments
    
    ##Create a loop that runs through each of the item in items
    for index, item in enumerate(items):
        snippet = item['snippet'] ##Get snippet from item parameter
        published_date = snippet['topLevelComment']['snippet']['publishedAt'].split('T')[0] ##Get published_date from the snippet variable and format the date
        pub_year = published_date.split('T')[0].split('-')[0] ##Get published year from the published_date variable and format the date
        pub_month = published_date.split('T')[0].split('-')[1] ##Get published month from the published_date variable and format the date
        ##Create a dictionary named comment_data for each of the item in items
        comment_data = {
            'author_display_name': snippet['topLevelComment']['snippet']['authorDisplayName'], ##Get author_display_name from snippet variable
            'top_level_comment': snippet['topLevelComment']['snippet']['textOriginal'], ##Get top_level_comment from snippet variable
            'top_level_comment_id': snippet['topLevelComment']['id'], ##Get top_level_comment_id from snippet variable
            'author_display_url': snippet['topLevelComment']['snippet']['authorProfileImageUrl'].replace('=s48-c-k-c0x00ffffff-no-rj',''),##Get author_display_url from snippet variable
            'like_count': snippet['topLevelComment']['snippet']['likeCount'],##Get like_count from snippet variable
            'published_date': published_date, ##Store published_date in published_date key in the dictionary
            'published_year': pub_year, ##Store published_date in published_date key in the dictionary
            'published_month': months[int(pub_month)-1], ##Store month name in published-month key in the dictionary
            'updated_at': snippet['topLevelComment']['snippet']['updatedAt'].split('T')[0], ##Store updated_at 
            'total_reply_count': snippet['totalReplyCount'] ##Store total_reply_count
        }
        
        ##Run this code block if the total_reply_count of the comment is greater than 0
        if(int(snippet['totalReplyCount']) > 0):
            comment_replies = get_comment_replies(snippet['topLevelComment']['id']) ##Get comment replies using get_comment_replies method and store in comment_replies variable
            ##Create loop to run till all reply in comment_replies
            for index1, reply in enumerate(comment_replies):
                comment_data[f'reply-{index1}'] =  reply['snippet']['textOriginal'] ##Get reply from the reply variable and store in comment_data
                comment_data[f'author_display_name-reply-{index1}']=reply['snippet']['authorDisplayName'] ##Get author_display_name from the reply variable and store in comment_data
            comments.append(comment_data) ##Add the comment_data to comments variable
        else: 
            comments.append(comment_data)  ##Add the comment_data to comments variable
    
    df = pd.DataFrame(comments) ##Create varible named df to convert comments to dataFrame using pandas library
    df.to_excel('results.xlsx', index=False) ##Use df variable to create an excel file name results.xlsx and write the contents to the file
    file = open('results.json', 'w', encoding='utf-8')##Create a file named results.json and open in write mode with utf-8 as character encoding
    file.write(json.dumps(comments, ensure_ascii=False, indent=4)) ##Write the results on results.json

##Run the main function
if __name__ == "__main__":
    main()
    