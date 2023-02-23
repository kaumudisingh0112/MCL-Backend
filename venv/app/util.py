from app.db import *
import boto3
from app.secrets import secrets
from botocore.client import Config
import boto3.session

def retrieve_data(data):
    bidder_data = get_bidder_data()    
    user_data = {}
    data = data["input"]

    user_data["city"] = data["City"]
    user_data["comp_categ"] = data["CompanyCategory"]
    user_data["contact_name"] = data["ContactName"]
    user_data["dob"] = data["DOB"]
    user_data["desig"] = data["Designation"]
    user_data["estb_year"] = data["EstablishmentYear"]
    user_data["legal_stat"] = data["LegalStatus"]
    user_data["partner_names"] = data["NameOfPartners"]
    user_data["busi_nature"] = data["NatureOfBusiness"]
    user_data["pan_no"] = data["PANNumber"]
    user_data["post_code"] = data["PostalCode"]
    user_data["reg_address"] = data["RegisteredAddress"]
    user_data["reg_no"] = data["RegistrationNumber"]
    user_data["state"] = data["State"]
    user_data["title"] = data["Title"]
    user_data["comp_name"] = data["companyName"]
    user_data["phone"] = data["phone"]
    user_data["prefix"] = data["prefix"]
    
    print(user_data)
    bidder_data.insert_one(user_data)
    print("Details inserted successfully!")

def upload_links(data):
    document_links = get_document_links()    
    links = {}
    
    links["pan"] = data["pan"]
    links["gst"] = data["gst"]
    links["sat_work"] = data["sat_work"]

    print(links)
    document_links.insert_one(links)
    print("Links inserted successfully!")



def create_presigned_url(expiration=3600):
    my_session = boto3.session.Session(aws_access_key_id=secrets['ACCESS_KEY'], aws_secret_access_key=secrets['SECRET_ACCESS_KEY'], region_name='ap-south-1')
    s3 = my_session.client('s3', config=Config(signature_version='s3v4'))
    url = s3.generate_presigned_url(
        ClientMethod='put_object',
        Params={
            'Bucket': 'shalakufileupload',
            'Key': 'key-name'
        },
        ExpiresIn=expiration
    )
    print(url)
    return url
