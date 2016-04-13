# MS Cognitive Services	- Recommendations API

Python implemntation of Microsoft's Cognitive Services sample application

Quick start guide for Cognitive Services Recommendations API

Follow instructions provided on quick start to create a Recommendations Cognitive Service. 

https://azure.microsoft.com/en-us/documentation/articles/cognitive-services-recommendations-quick-start/

Sample Application originally coded in C# can be obtained from:
http://go.microsoft.com/fwlink/?LinkID=759344

In order to use the recommendations API you need to take the following steps:

1. Create a Model
2. Import Catalog Data
3. Import Usage Data
4. Build a recommendation model
5. Consume Recommendations


## Sample output

```
RecommendationAPIWrapper
Created Model id :  48566869-07f6-40a4-80ef-49fff05f3128

Upload Feature Catalog
Processed Line Count: 2929 
Imported Line Count : 2929 
Error Line Count : 0

Upload Usage Data
Processed Line Count: 85169 
Imported Line Count : 85169 
Error Line Count : 0

Build Model
WaitForBuildCompletion
Waiting for 40 sec for propagation of the built model...

Getting Item to Item Recommendations for The Piano Man's Daughter
item id: 679722319 
Item Name : Where I'm Calling from: New and Selected Stories (Vintage Contemporaries) 
Rating : 0.605084 
item id: 60981180 
Item Name : Mariette in Ecstasy 
Rating : 0.598220 
item id: 671792806 
Item Name : PRINCIPLE CENTERED LEADERSHIP 
Rating : 0.597580 
item id: 60958022 
Item Name : Five Quarters of the Orange 
Rating : 0.597529 
item id: 60925000 
Item Name : A Suitable Boy : Novel A 
Rating : 0.597114 
item id: 671683993 
Item Name : The Temple of My Familiar 
Rating : 0.597001 

Getting User Recommendations for User: 142256
item id: 671786601 
Item Name : To Trust a Stranger 
Rating : 0.801583 
item id: 61098361 
Item Name : Circle of Three: A Novel 
Rating : 0.798545 
item id: 671793578 
Item Name : The End Of The Dream The Golden Boy Who Never Grew Up : Ann Rules Crime Files Volume 5 
Rating : 0.794534 
item id: 671868691 
Item Name : Bitter Harvest 
Rating : 0.781504 
item id: 61097101 
Item Name : The Saving Graces: A Novel 
Rating : 0.776046 
item id: 61031445 
Item Name : Flight Lessons 
Rating : 0.772279 

```