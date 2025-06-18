


body = ''' 

    Input files:
	1.	Reel video(.mp4)
    2.  Tags      (.txt)
	3.	Thumbnail (.jpeg) 
  
Examine the audio transcript,caption and thumbnail on screen text to categorise the content into several categories.
If the content does not fit a category or description, just put none.
From the Tags, analyise the creator country and language. Place content under "Geograhical Region/Language" only is there is some content,
which is not part of his native region/language
if the category3 is spanish, not include it --> None.

Category 1
	1.	audio_language_toxicity
	2.	Caption_language_toxicity
	3.	hate_speech_aggression
	4.	Sexual_indecent_content
	5.	Substances. 

Category2:
	1.	abuse/assault
	2.	Arrest
	3.	Bullying
	4.	Disregard for human life 
	5.	Fear mongering
	6.	Human trafficking 
	7.	Political figure
	8.	Region
	9.	Transphobia
	10.	Sustainability

Category3:
	1.	child endangerment
	2.	Controversial political/social topic
	3.	Geograhical Region/Language
	4.	Natural/organic 
	5.	Political figure 

Response format: 
<category1>,<description of catergory1 >, <category2>, <description of Category2>, <category3>, <description of category3> <describe the video in 5-7words>
 

'''


body1 = '''
        complete audio transcript as well as ocr text. Both in english and spanish. JSON format. (THis for .mp4 file)
        Translation of (.txt) file in english.
       '''
