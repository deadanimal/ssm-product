import requests
import json
import xmltodict

def get_basic_company_profile(url, headers, registration_number, check_digit):

    payload = """
        <soapenv:Envelope xmlns:soapenv=\"http://schemas.xmlsoap.org/soap/envelope/\" xmlns:ws=\"http://integrasistg.ssm.com.my/InfoService/1/WS\">
        <soapenv:Header/>
        <soapenv:Body>
            <ws:getBasicCompProf>
                <header>
                    <customerId>SSMProduk</customerId>            
                    <customerReferenceNo>FAHMITEST</customerReferenceNo>
                    <customerRequestDate>2018-10-29T00:00:00</customerRequestDate>      
                </header>
                <request>           
                    <supplyInfoReq>               
                        <checkDigit>P</checkDigit>            
                        <gstAmount>0</gstAmount>               
                        <infoAmount>0</infoAmount>
                        <invoiceNo></invoiceNo>
                        <ipaddress></ipaddress>
                        <lastUpdateDate></lastUpdateDate>
                        <regNo>1097967</regNo>
                        <remark></remark>
                        <tableId>ROCINFO</tableId>
                        <type>INFOPROFILE</type>
                    </supplyInfoReq>
                </request>      
            </ws:getBasicCompProf>
        </soapenv:Body>
        </soapenv:Envelope>
    """

    response = requests.request("POST", url, data=payload, headers=headers)
    response_xml = response.content
    
    from xml.dom import minidom                                          
    xmldoc = minidom.parseString(payload)  
    #print(xmldoc.getroot())
    #print(xmldoc)
        
    sample_response = """
   <soapenv:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/">
   <soapenv:Header/>
   <soapenv:Body>
      <inf:getBasicCompProfResponse xmlns:inf="http://integrasistg.ssm.com.my/InfoService/1/WS" xmlns:soapenc="http://schemas.xmlsoap.org/soap/encoding/">
         <header>
            <customerId>SSMProduk</customerId>
            <customerReferenceNo>FAHMITEST</customerReferenceNo>
            <customerRequestDate>2018-10-29T00:00:00</customerRequestDate>
            <errorCode/>
            <errorMessage/>
            <hostErrorCode/>
            <hostErrorMessage/>
            <requestTimestamp>2020-08-29T22:41:33.750</requestTimestamp>
            <responseTimestamp>2020-08-29T22:41:33.927</responseTimestamp>
         </header>
         <request>
            <supplyInfoReq>
               <checkDigit>P</checkDigit>
               <gstAmount>0</gstAmount>
               <infoAmount>0</infoAmount>
               <invoiceNo>?</invoiceNo>
               <ipaddress>?</ipaddress>
               <regNo>1097967</regNo>
               <remark>?</remark>
               <tableId/>
               <type/>
            </supplyInfoReq>
         </request>
         <response>
            <GetBasicCompProfReturn xsi:type="inf:companyInfoProfile">
               <errorMsg/>
               <infoId>38621844</infoId>
               <successCode>00</successCode>
               <rocCompanyInfo>
                  <errorMsg/>
                  <infoId/>
                  <lastUpdateDate>2019-03-02T16:30:53.000Z</lastUpdateDate>
                  <successCode>00</successCode>
                  <balaceSheetInfo/>
                  <balaceSheetInfoDesc/>
                  <businessDescription>1.TRAVELLING
2.GENERAL TRADING &amp; SERVICES
3.INVESTMENT HOLDINGS</businessDescription>
                  <checkDigit>P</checkDigit>
                  <companyCountry>MAL</companyCountry>
                  <companyName>ALL ASIA TRAVEL &amp; TOURS SDN. BHD.</companyName>
                  <companyNo>1097967</companyNo>
                  <companyOldName/>
                  <companyStatus>R</companyStatus>
                  <companyType>S</companyType>
                  <currency>RM</currency>
                  <incomeStatInfo/>
                  <incomeStatInfoDesc/>
                  <incorpDate>2014-06-16T16:00:00.000Z</incorpDate>
                  <infoColon/>
                  <latestDocUpdateDate>2018-07-25T03:47:33.000Z</latestDocUpdateDate>
                  <llpInfo/>
                  <llpInfoDesc/>
                  <llpName/>
                  <llpNo/>
                  <localforeignCompany>L</localforeignCompany>
                  <naBal/>
                  <naProf/>
                  <registrationDate>2014-06-16T16:00:00.000Z</registrationDate>
                  <statusOfCompany>E</statusOfCompany>
                  <wupType/>
               </rocCompanyInfo>
               <rocRegAddressInfo>
                  <errorMsg/>
                  <infoId/>
                  <lastUpdateDate>2017-04-20T03:42:52.000Z</lastUpdateDate>
                  <successCode>00</successCode>
                  <address1>NO. 5-4-2, JALAN 2/50</address1>
                  <address2>DIAMOND SQUARE</address2>
                  <address3>OFF JALAN GOMBAK</address3>
                  <companyNo>1097967</companyNo>
                  <postcode>53000</postcode>
                  <state>W</state>
                  <town>KUALA LUMPUR</town>
               </rocRegAddressInfo>
               <rocBusinessAddressInfo>
                  <errorMsg/>
                  <infoId/>
                  <lastUpdateDate>2018-07-25T03:47:33.000Z</lastUpdateDate>
                  <successCode>00</successCode>
                  <address1>28-1, JALAN 4/76C</address1>
                  <address2>DESA PANDAN</address2>
                  <address3/>
                  <companyNo>1097967</companyNo>
                  <postcode>55100</postcode>
                  <state>W</state>
                  <town>KUALA  LUMPUR</town>
               </rocBusinessAddressInfo>
            </GetBasicCompProfReturn>
         </response>
      </inf:getBasicCompProfResponse>
   </soapenv:Body>
</soapenv:Envelope>
"""

    middleware_response_json = json.loads(json.dumps(xmltodict.parse(sample_response)))
    return middleware_response_json['soapenv:Envelope']['soapenv:Body']['inf:getBasicCompProfResponse']['response']['GetBasicCompProfReturn']