import googleapiclient.discovery
import pprint, json, time
import pandas as pd

api_service_name = "youtube"
api_version = "v3"
DEVELOPER_KEY = "AIzaSyBighmBrEqkN4wkPGIhv_9zC9eQm1pf7nc"
video_id = "TATSAHJKRd8"

youtube = googleapiclient.discovery.build(
api_service_name, api_version, developerKey = DEVELOPER_KEY)
months = ['Jan','Feb','Mar','Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

def main():
    request = youtube.commentThreads().list(
        part="snippet, replies",
        videoId=video_id,
        maxResults=100)
        
    response = request.execute()
    
    file = open('results-raw.json', 'w', encoding='utf-8')
    file.write(json.dumps(response, ensure_ascii=False, indent=4))
    
    all_comments = response.get('items')
    
    has_next_page = 'nextPageToken' in response
    next_page_token = response.get('nextPageToken') 
    
    if has_next_page is True:
        next_page_comments = get_all_comments(video_id=video_id,next_page_token=next_page_token, max_results=100, has_next_page=has_next_page)
        all_comments.extend(next_page_comments)
        scrape_comments(all_comments)
        
    else:
        scrape_comments(all_comments)
        
def get_all_comments(video_id, max_results,next_page_token, has_next_page):
    comments = []
    while has_next_page:
        request = youtube.commentThreads().list(
        part="snippet, replies",
        videoId=video_id,
        maxResults=max_results,
        pageToken=next_page_token)
        
        response = request.execute()
        items = response.get('items')
        comments.extend(items)
        
        next_page_token = response.get('nextPageToken') 
        has_next_page = 'nextPageToken' in response
    return comments
    
def get_comment_replies(parent_video_id):
    replies = []
    response = youtube.comments().list(
        part='snippet',
        maxResults= 100,
        parentId = parent_video_id,        
    ).execute()
    replies.extend(response.get('items'))    
    has_next_page = 'nextPageToken' in response
    next_page_token = response.get('nextPageToken')
    
    if has_next_page is True:
        while has_next_page:
            request = youtube.comments().list(
            part="snippet",
            parentId = parent_video_id,
            maxResults=100,
            pageToken=next_page_token)
            
            response = request.execute()
            items = response.get('items')
            replies.extend(items)
            
            next_page_token = response.get('nextPageToken') 
            has_next_page = 'nextPageToken' in response
        return replies    
    else:
        return replies    

def scrape_comments(items): 
    comments = []
    
    for index, item in enumerate(items):
        snippet = item['snippet']
        published_date = snippet['topLevelComment']['snippet']['publishedAt'].split('T')[0]
        pub_year = published_date.split('T')[0].split('-')[0]
        pub_month = published_date.split('T')[0].split('-')[1]
        comment_data = {
            'author_display_name': snippet['topLevelComment']['snippet']['authorDisplayName'],
            'top_level_comment': snippet['topLevelComment']['snippet']['textOriginal'],
            'top_level_comment_id': snippet['topLevelComment']['id'],
            'author_display_url': snippet['topLevelComment']['snippet']['authorProfileImageUrl'].replace('=s48-c-k-c0x00ffffff-no-rj',''),
            'like_count': snippet['topLevelComment']['snippet']['likeCount'],
            'published_date': published_date,
            'published_year': pub_year,
            'published_month': months[int(pub_month)-1],
            'updated_at': snippet['topLevelComment']['snippet']['updatedAt'].split('T')[0],
            'total_reply_count': snippet['totalReplyCount']
        }
        
        
        if(int(snippet['totalReplyCount']) > 0):
            comment_replies = get_comment_replies(snippet['topLevelComment']['id'])
            for index1, reply in enumerate(comment_replies):
                comment_data[f'reply-{index1}'] =  reply['snippet']['textOriginal']
                comment_data[f'author_display_name-reply-{index1}']=reply['snippet']['authorDisplayName']
            comments.append(comment_data) 
        else: 
            comments.append(comment_data) 
    
    df = pd.DataFrame(comments)
    df.to_excel('results.xlsx', index=False)
    file = open('results.json', 'w', encoding='utf-8')
    file.write(json.dumps(comments, ensure_ascii=False, indent=4))

if __name__ == "__main__":
    main()
    