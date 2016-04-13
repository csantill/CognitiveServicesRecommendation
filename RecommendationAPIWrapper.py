#!/usr/bin/python
# -*- coding: utf-8 -*-
"""

@author: Carlos Santillan <csantill@gmail.com>

Python implementation of Sample application for Microsoft's Recommender 
Cognitive Service.

For more information: 

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

import requests
import json
import time


class RecommendationAPIWrapper:

    def __init__(self, accountKey):
        self.headers= { # Request headers
                        'Content-Type': 'application/json',
                        'Ocp-Apim-Subscription-Key': accountKey,
                     }
        self.baseModelURL = 'https://westus.api.cognitive.microsoft.com/recommendations/v4.0/models'
        self.operationsBaseURL ='https://westus.api.cognitive.microsoft.com/recommendations/v4.0/operations'
        
        
        

    def CreateModel(self,modelName,modelDescription):
        try:
            data = { "modelName": modelName,  "description": modelDescription}
            r=requests.post(self.baseModelURL,json=data ,  headers=self.headers)
            r.raise_for_status()
            jsonresponse = json.loads(r.text)
            return jsonresponse['id']        
        except Exception as e:
            print str(e)
            
    def DeleteModel(self,modelId)  :      
        try:
            r=requests.delete(self.baseModelURL+'/'+modelId,  headers=self.headers)
            r.raise_for_status()
            return r
        except Exception as e:
            print str(e)
            
    def GetAllModels(self):
        try:
            r=requests.get(self.baseModelURL,  headers=self.headers)
            r.raise_for_status()
            return r
        except Exception as e:
            print str(e)
            
    def UploadCatalog(self,modelId, CatalogFile, DisplayName):
        url=self.baseModelURL+'/'+modelId+'/catalog?catalogDisplayName=' +DisplayName
        try:
            with open(CatalogFile,'rb') as f:
                r= requests.post(url,data=f.read(),headers=self.headers)
            r.raise_for_status()            
            return json.loads(r.text)  
        except Exception as e:
            print str(e)
                
    def UploadUsage(self,modelId, UsageFile, DisplayName):
        url=self.baseModelURL+'/'+modelId+'/usage?usageDisplayName=' +DisplayName
        try:
            with open(UsageFile,'rb') as f:
                r= requests.post(url,data=f.read(),headers=self.headers)
            r.raise_for_status()    
            return json.loads(r.text)
        except Exception as e:
            print str(e)

           
    def BuildModel(self,modelId,params):
        url=self.baseModelURL+'/'+modelId+'/builds' 
        try:
            r= requests.post(url,json=params,headers=self.headers)
            r.raise_for_status()
            jsonresponse = json.loads(r.text)
           
            return jsonresponse['buildId']
        except Exception as e:
            print str(e)
            
    def WaitForBuildCompletion(self,buildId):
        url = self.operationsBaseURL +'/'+str(buildId)
        status = None
        print "WaitForBuildCompletion"
        while True:
            r=requests.get(url,  headers=self.headers)
            r.raise_for_status()
            jsonresponse = json.loads(r.text)
            status = jsonresponse['status']
            if (status == 'Succeeded' or status == 'Failed' or status == 'Cancelled') :
                break
            time.sleep(10) # Wait 10 seconds before we check again
        return status
            
    def SetActiveBuild(self,modelId,buildId):
        url=self.baseModelURL+'/'+modelId
        data = { "ActiveBuildId": buildId}
        try:
            r= requests.patch(url,json=data,headers=self.headers)
            r.raise_for_status()
            #jsonresponse = json.loads(r.text)
           
            return r
        except Exception as e:
            print str(e)
     
    def GetRecomendations(self,modelId,buildId,itemIds,numberOfResults):
        url=self.baseModelURL+'/'+modelId +'/recommend/item?itemIds='+itemIds+'&numberOfResults='+numberOfResults+'&minimalScore=0'
        try:
           r=requests.get(url,  headers=self.headers)
           r.raise_for_status()
           return json.loads(r.text)
        except Exception as e:
           print str(e)
        
    def GetUserRecommendations(self,modelId,buildId,userId,numberOfResults):
        url=self.baseModelURL+'/'+modelId +'/recommend/user?userId='+userId+'&numberOfResults='+numberOfResults
        try:
           r=requests.get(url,  headers=self.headers)
           r.raise_for_status()
           return json.loads(r.text)
        except Exception as e:
           print str(e)            
            
            
                
