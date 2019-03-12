from clarifai.rest import ClarifaiApp

app = ClarifaiApp()

def get_relevant_tags(image_url):
    response_data = app.tag_urls([image_url])

    tag_urls = []
    for concept in response_data['outputs'][0]['data']['concepts']:
        tag_urls.append(concept['name'])
    
    return tag_urls
print('\n'.join(get_relevant_tags('https://images.unsplash.com/photo-1552197956-eb7334216110?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1234&q=80')))