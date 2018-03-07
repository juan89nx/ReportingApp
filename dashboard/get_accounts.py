from googleads import adwords

adwords_client = adwords.AdWordsClient.LoadFromStorage()

service = adwords_client.GetService('ManagedCustomerService', version='v201710')
selector = {
            'fields': ['CustomerId', 'Name'],
            'paging':
            {
              'startIndex': '0',
              'numberResults': '10'
            },
        }
page = service.get(selector)
