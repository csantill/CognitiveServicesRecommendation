# -*- coding: utf-8 -*-
"""
@author: Carlos Santillan <csantill@gmail.com>

Python implementation of Sample application for Microsoft's Recommender 
Cognitive Service.

For more information 

https://azure.microsoft.com/en-us/documentation/articles/cognitive-services-recommendations-quick-start/

Original C# code can be found 
http://go.microsoft.com/fwlink/?LinkID=759344


Copyright (C) 2016 Carlos Santillan <csantill@gmail.com>

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""

import RecommendationAPIWrapper as Azrecommender
import time


def printRecommendations(recommendationItems):
    for rec in recommendationItems['recommendedItems']:
            for item in rec['items']:
                print 'item id: %s \nItem Name : %s \nRating : %f ' % (item['id'] ,  item['name'],  rec['rating'])
                

def printUploadSummary(UploadLog):
    print 'Processed Line Count: %d \nImported Line Count : %d ' % (UploadLog['processedLineCount'] ,  UploadLog['importedLineCount'])
    print 'Error Line Count : %d' % UploadLog['errorLineCount'] 
    

def main():
    AccountKey=''   #Enter your API key here.  
    modelId = None
    recommender=Azrecommender.RecommendationAPIWrapper(AccountKey)
    try:
        #Create the Model
        modelId=recommender.CreateModel('MyModel','Sample model')
        print 'Created Model id :  %s' % modelId
        # Load Catalog
        print '\nUpload Feature Catalog'        
        importCatalogStats=recommender.UploadCatalog(modelId,'data/catalog_small.csv','catalog_small.csv')
        printUploadSummary(importCatalogStats)
        # Load Usage
        print '\nUpload Usage Data'
        importUsageStats= recommender.UploadUsage(modelId,'data/usage_small.csv','usage_small.csv')
        
        printUploadSummary(importUsageStats)
        print '\nBuild Model'
        # Model Parameter information can be found at
        # https://westus.dev.cognitive.microsoft.com/docs/services/Recommendations.V4.0/operations/56f30d77eda5650db055a3d0/console
        params = {
             "description": "Build 1",
             "buildType": "recommendation",
             "buildParameters": {
                 "recommendation": {
                     "numberOfModelIterations": 10,
                     "numberOfModelDimensions": 20,
                     "itemCutOffLowerBound": 1,
                     "enableModelingInsights": False,
                     "enableU2I": True,
                     "useFeaturesInModel": False,
                     "allowColdItemPlacement": False
                     } 
              }
        }
        
        buildId = recommender.BuildModel(modelId,params)        
        
        status= recommender.WaitForBuildCompletion(buildId)
        if status != 'Succeeded':
            print 'Build %d did not end successfully, the sample app will stop here' %buildId
            return
       
        print 'Waiting for 40 sec for propagation of the built model...'
        time.sleep(40) # Wait 40 seconds
        recommender.SetActiveBuild(modelId,buildId)
        
        #Get item to item recommendations. (I2I)
        print "\nGetting Item to Item Recommendations for The Piano Man's Daughter"
        itemids = '6485200'
        resjson =recommender.GetRecomendations(modelId,buildId,itemids,'6')
        printRecommendations(resjson)
                
        #Now let's get a user recommendation (U2I)
        userId = "142256"
        
        print '\nGetting User Recommendations for User: 142256'
        resjson =recommender.GetUserRecommendations(modelId,buildId,userId,'6')
        
        printRecommendations(resjson)
    finally:
        if modelId != None:
             # Uncomment the line below if you wish to delete the model.
             # Note that you can have up to 10 models at any time. 
             # You may have up to 20 builds per model.            
            recommender.DeleteModel(modelId)                        
    
            



res = main()

