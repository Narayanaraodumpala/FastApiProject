from typing import Union,Optional

from fastapi import FastAPI, File, UploadFile
import uvicorn
import os
import csv

from io import StringIO
from dotenv import load_dotenv
from sqlalchemy import and_
from starlette.responses import Response

from fastapi.middleware.cors import CORSMiddleware
from fastapi_sqlalchemy import DBSessionMiddleware, db
from fastapi_pagination import Page, paginate, add_pagination, Params

from sql_app.models import NationalProviderIdentifier as ModelNationalProviderIdentifier
from sql_app.models import NPIProviderData
from sql_app.models import NPIHospitalData
from sql_app.schemas import NPIProviderData as SchemaNPIProviderData
from sql_app.schemas import NPIHospitalData as SchemaNPIHospitalData


app = FastAPI(
    version="1.1",
    title="npi-data",
    description="Npi Data Based Microservice",
)

add_pagination(app)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from . import crud, models, schemas
from sql_app.database import SessionLocal, engine
# from fastapi_sqlalchemy import DBSessionMiddleware, db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# to avoid csrftokenError
DATABASE_URL = 'postgresql+psycopg2://postgres:postgres@localhost:5433/revision_db'
app.add_middleware(DBSessionMiddleware, db_url=DATABASE_URL)

# app.add_middleware(DBSessionMiddleware, db_url=os.environ['DATABASE_URL'])

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.User)
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)




@app.get("/users/", response_model=list[schemas.User])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users

@app.get("/allusers/", response_model=list[schemas.User])
def read_users( db: Session = Depends(get_db)):
    users = crud.get_users(db, )
    return users


@app.get("/users/{user_id}", response_model=schemas.User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.post("/users/{user_id}/items/", response_model=schemas.Item)
def create_item_for_user(
    user_id: int, item: schemas.ItemCreate, db: Session = Depends(get_db)
):
    return crud.create_user_item(db=db, item=item, user_id=user_id)


@app.get("/items/", response_model=list[schemas.Item])
def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    items = crud.get_items(db, skip=skip, limit=limit)
    return items



#npi data code 


@app.get("/")
async def root():
    return {"message": "npi data microservice"}


@app.post("/api/v1/upload-npi-data/")
async def upload(file: UploadFile = File(...)):
   
    try:
        
        data = {}
        contents = file.file.read()
        buffer = StringIO(contents.decode('utf-8'))
        csvReader = csv.DictReader(buffer)
        for row in csvReader:
           
            db_npi = ModelNationalProviderIdentifier(npi_id=row['NPI'],
                                                     endpoint_type=row['Endpoint Type'],
                                                     endpoint_type_description=row['Endpoint Type Description'],
                                                     endpoint=row['Endpoint'],
                                                     affiliation=row['Affiliation'],
                                                     endpoint_description=row['Endpoint Description'],
                                                     affiliation_legal_business_name=row[
                                                         'Affiliation Legal Business Name'],
                                                     use_code=row['Use Code'],
                                                     use_description=row['Use Description'],
                                                     other_use_description=row['Other Use Description'],
                                                     content_type=row['Content Type'],
                                                     content_description=row['Content Description'],
                                                     other_content_description=row['Other Content Description'],
                                                     affiliation_address_line_one=row[
                                                         'Affiliation Address Line One'],
                                                     affiliation_address_line_two=row[
                                                         'Affiliation Address Line Two'],
                                                     affiliation_address_city=row['Affiliation Address City'],
                                                     affiliation_address_state=row['Affiliation Address State'],
                                                     affiliation_address_country=row[
                                                         'Affiliation Address Country'],
                                                     affiliation_address_postal_code=row[
                                                         'Affiliation Address Postal Code'],

                                                     )
            db.session.add(db_npi)
            db.session.commit()
            key = row['NPI']
            data[key] = row

        buffer.close()
        file.file.close()
        return data

    except Exception:
        return Response("Internal server error", status_code=500)


def search_npi_id(query: str):
    npi_id = db.session.query(ModelNationalProviderIdentifier).filter(
        ModelNationalProviderIdentifier.npi_id.contains(query))
    return npi_id


@app.get("/api/v1/search/")
def search(query: Optional[str] = None):
    if query:
        search_query = db.session.query(
            ModelNationalProviderIdentifier).filter(
            ModelNationalProviderIdentifier.npi_id.contains(query)
        ).all() or db.session.query(
            ModelNationalProviderIdentifier).filter(
            ModelNationalProviderIdentifier.affiliation_legal_business_name.contains(query)
        ).all() or db.session.query(
            ModelNationalProviderIdentifier).filter(
            ModelNationalProviderIdentifier.endpoint.contains(query)
        ).all() or db.session.query(
            ModelNationalProviderIdentifier).filter(
            ModelNationalProviderIdentifier.endpoint_description.contains(query)
        ).all() or db.session.query(
            ModelNationalProviderIdentifier).filter(
            ModelNationalProviderIdentifier.affiliation_address_city.contains(query)
        ).all()
        db.session.close()

        return search_query
    else:
        search_query = db.session.query(
            ModelNationalProviderIdentifier).filter(
            ModelNationalProviderIdentifier.npi_id).limit(10).all()
        db.session.close()
        return search_query


@app.post("/api/v1/upload-npi-main-data/")
async def upload_npi(file: UploadFile = File(...)):
    try:
        data = {}
        contents = file.file.read()
        buffer = StringIO(contents.decode('utf-8'))
        csvReader = csv.DictReader(buffer)
        for row in csvReader:
            print('request arrived ----')
            db_npi = NPIProviderData(npi=row['NPI'],
                                     entity_type_code=row['Entity Type Code'],
                                     replacement_npi=row['Replacement NPI'],
                                     employer_identification_number_ein=row[
                                         'Employer Identification Number (EIN)'],
                                     provider_organization_name_legal_business_name=row[
                                         'Provider Organization Name (Legal Business Name)'],
                                     provider_last_name_legal_name=row[
                                         'Provider Last Name (Legal Name)'],
                                     provider_first_name=row['Provider First Name'],
                                     provider_middle_name=row['Provider Middle Name'],
                                     provider_name_prefix_text=row['Provider Name Prefix Text'],
                                     provider_name_suffix_text=row['Provider Name Suffix Text'],
                                     provider_credential_text=row['Provider Credential Text'],
                                     provider_other_organization_name=row[
                                         'Provider Other Organization Name'],
                                     provider_other_organization_name_type_code=row[
                                         'Provider Other Organization Name Type Code'],
                                     provider_other_last_name=row['Provider Other Last Name'],
                                     provider_other_first_name=row['Provider Other First Name'],
                                     provider_other_middle_name=row[
                                         'Provider Other Middle Name'],
                                     provider_other_name_prefix_text=row[
                                         'Provider Other Name Prefix Text'],
                                     provider_other_name_suffix_text=row[
                                         'Provider Other Name Suffix Text'],
                                     provider_other_credential_text=row[
                                         'Provider Other Credential Text'],
                                     provider_other_last_name_type_code=row[
                                         'Provider Other Last Name Type Code'],
                                     provider_first_line_business_mailing_address=row[
                                         'Provider First Line Business Mailing Address'],
                                     provider_second_line_business_mailing_address=row[
                                         'Provider Second Line Business Mailing Address'],
                                     provider_business_mailing_address_city_name=row[
                                         'Provider Business Mailing Address City Name'],
                                     provider_business_mailing_address_state_name=row[
                                         'Provider Business Mailing Address State Name'],
                                     provider_business_mailing_address_postal_code=row[
                                         'Provider Business Mailing Address Postal Code'],
                                     provider_business_mailing_address_country_code_if_outside_u_s=
                                     row[
                                         'Provider Business Mailing Address Country Code (If outside U.S.)'],
                                     provider_business_mailing_address_telephone_number=row[
                                         'Provider Business Mailing Address Telephone Number'],
                                     provider_business_mailing_address_fax_number=row[
                                         'Provider Business Mailing Address Fax Number'],
                                     provider_first_line_business_practice_location_address=row[
                                         'Provider First Line Business Practice Location Address'],
                                     provider_second_line_business_practice_location_address=row[
                                         'Provider Second Line Business Practice Location Address'],
                                     provider_business_practice_location_address_city_name=row[
                                         'Provider Business Practice Location Address City Name'],
                                     provider_business_practice_location_address_state_name=row[
                                         'Provider Business Practice Location Address State Name'],
                                     provider_business_practice_location_address_postal_code=row[
                                         'Provider Business Practice Location Address Postal Code'],
                                     provider_business_practice_location_address_country_code_if_outside_u_s=
                                     row[
                                         'Provider Business Practice Location Address Country Code (If outside U.S.)'],
                                     provider_business_practice_location_address_telephone_number=
                                     row[
                                         'Provider Business Practice Location Address Telephone Number'],
                                     provider_business_practice_location_address_fax_number=row[
                                         'Provider Business Practice Location Address Fax Number'],
                                     provider_enumeration_date=row['Provider Enumeration Date'],
                                     last_update_date=row['Last Update Date'],
                                     npi_deactivation_reason_code=row[
                                         'NPI Deactivation Reason Code'],
                                     npi_deactivation_date=row['NPI Deactivation Date'],
                                     npi_reactivation_date=row['NPI Reactivation Date'],
                                     provider_gender_code=row['Provider Gender Code'],
                                     authorized_official_last_name=row[
                                         'Authorized Official Last Name'],
                                     authorized_official_first_name=row[
                                         'Authorized Official First Name'],
                                     authorized_official_middle_name=row[
                                         'Authorized Official Middle Name'],
                                     authorized_official_title_or_position=row[
                                         'Authorized Official Title or Position'],
                                     authorized_official_telephone_number=row[
                                         'Authorized Official Telephone Number'],
                                     healthcare_provider_taxonomy_code_1=row[
                                         'Healthcare Provider Taxonomy Code_1'],
                                     provider_license_number_1=row['Provider License Number_1'],
                                     provider_license_number_state_code_1=row[
                                         'Provider License Number State Code_1'],
                                     healthcare_provider_primary_taxonomy_switch_1=row[
                                         'Healthcare Provider Primary Taxonomy Switch_1'],
                                     healthcare_provider_taxonomy_code_2=row[
                                         'Healthcare Provider Taxonomy Code_2'],
                                     provider_license_number_2=row['Provider License Number_2'],
                                     provider_license_number_state_code_2=row[
                                         'Provider License Number State Code_2'],
                                     healthcare_provider_primary_taxonomy_switch_2=row[
                                         'Healthcare Provider Primary Taxonomy Switch_2'],
                                     healthcare_provider_taxonomy_code_3=row[
                                         'Healthcare Provider Taxonomy Code_3'],
                                     provider_license_number_3=row['Provider License Number_3'],
                                     provider_license_number_state_code_3=row[
                                         'Provider License Number State Code_3'],
                                     healthcare_provider_primary_taxonomy_switch_3=row[
                                         'Healthcare Provider Primary Taxonomy Switch_3'],
                                     healthcare_provider_taxonomy_code_4=row[
                                         'Healthcare Provider Taxonomy Code_4'],
                                     provider_license_number_4=row['Provider License Number_4'],
                                     provider_license_number_state_code_4=row[
                                         'Provider License Number State Code_4'],
                                     healthcare_provider_primary_taxonomy_switch_4=row[
                                         'Healthcare Provider Primary Taxonomy Switch_4'],
                                     healthcare_provider_taxonomy_code_5=row[
                                         'Healthcare Provider Taxonomy Code_5'],
                                     provider_license_number_5=row['Provider License Number_5'],
                                     provider_license_number_state_code_5=row[
                                         'Provider License Number State Code_5'],
                                     healthcare_provider_primary_taxonomy_switch_5=row[
                                         'Healthcare Provider Primary Taxonomy Switch_5'],
                                     healthcare_provider_taxonomy_code_6=row[
                                         'Healthcare Provider Taxonomy Code_6'],
                                     provider_license_number_6=row['Provider License Number_6'],
                                     provider_license_number_state_code_6=row[
                                         'Provider License Number State Code_6'],
                                     healthcare_provider_primary_taxonomy_switch_6=row[
                                         'Healthcare Provider Primary Taxonomy Switch_6'],
                                     healthcare_provider_taxonomy_code_7=row[
                                         'Healthcare Provider Taxonomy Code_7'],
                                     provider_license_number_7=row['Provider License Number_7'],
                                     provider_license_number_state_code_7=row[
                                         'Provider License Number State Code_7'],
                                     healthcare_provider_primary_taxonomy_switch_7=row[
                                         'Healthcare Provider Primary Taxonomy Switch_7'],
                                     healthcare_provider_taxonomy_code_8=row[
                                         'Healthcare Provider Taxonomy Code_8'],
                                     provider_license_number_8=row['Provider License Number_8'],
                                     provider_license_number_state_code_8=row[
                                         'Provider License Number State Code_8'],
                                     healthcare_provider_primary_taxonomy_switch_8=row[
                                         'Healthcare Provider Primary Taxonomy Switch_8'],
                                     healthcare_provider_taxonomy_code_9=row[
                                         'Healthcare Provider Taxonomy Code_9'],
                                     provider_license_number_9=row['Provider License Number_9'],
                                     provider_license_number_state_code_9=row[
                                         'Provider License Number State Code_9'],
                                     healthcare_provider_primary_taxonomy_switch_9=row[
                                         'Healthcare Provider Primary Taxonomy Switch_9'],
                                     healthcare_provider_taxonomy_code_10=row[
                                         'Healthcare Provider Taxonomy Code_10'],
                                     provider_license_number_10=row[
                                         'Provider License Number_10'],
                                     provider_license_number_state_code_10=row[
                                         'Provider License Number State Code_10'],
                                     healthcare_provider_primary_taxonomy_switch_10=row[
                                         'Healthcare Provider Primary Taxonomy Switch_10'],
                                     healthcare_provider_taxonomy_code_11=row[
                                         'Healthcare Provider Taxonomy Code_11'],
                                     provider_license_number_11=row[
                                         'Provider License Number_11'],
                                     provider_license_number_state_code_11=row[
                                         'Provider License Number State Code_11'],
                                     healthcare_provider_primary_taxonomy_switch_11=row[
                                         'Healthcare Provider Primary Taxonomy Switch_11'],
                                     healthcare_provider_taxonomy_code_12=row[
                                         'Healthcare Provider Taxonomy Code_12'],
                                     provider_license_number_12=row[
                                         'Provider License Number_12'],
                                     provider_license_number_state_code_12=row[
                                         'Provider License Number State Code_12'],
                                     healthcare_provider_primary_taxonomy_switch_12=row[
                                         'Healthcare Provider Primary Taxonomy Switch_12'],
                                     healthcare_provider_taxonomy_code_13=row[
                                         'Healthcare Provider Taxonomy Code_13'],
                                     provider_license_number_13=row[
                                         'Provider License Number_13'],
                                     provider_license_number_state_code_13=row[
                                         'Provider License Number State Code_13'],
                                     healthcare_provider_primary_taxonomy_switch_13=row[
                                         'Healthcare Provider Primary Taxonomy Switch_13'],
                                     healthcare_provider_taxonomy_code_14=row[
                                         'Healthcare Provider Taxonomy Code_14'],
                                     provider_license_number_14=row[
                                         'Provider License Number_14'],
                                     provider_license_number_state_code_14=row[
                                         'Provider License Number State Code_14'],
                                     healthcare_provider_primary_taxonomy_switch_14=row[
                                         'Healthcare Provider Primary Taxonomy Switch_14'],
                                     healthcare_provider_taxonomy_code_15=row[
                                         'Healthcare Provider Taxonomy Code_15'],
                                     provider_license_number_15=row[
                                         'Provider License Number_15'],
                                     provider_license_number_state_code_15=row[
                                         'Provider License Number State Code_15'],
                                     healthcare_provider_primary_taxonomy_switch_15=row[
                                         'Healthcare Provider Primary Taxonomy Switch_15'],
                                     other_provider_identifier_1=row[
                                         'Other Provider Identifier_1'],
                                     other_provider_identifier_type_code_1=row[
                                         'Other Provider Identifier Type Code_1'],
                                     other_provider_identifier_state_1=row[
                                         'Other Provider Identifier State_1'],
                                     other_provider_identifier_issuer_1=row[
                                         'Other Provider Identifier Issuer_1'],
                                     other_provider_identifier_2=row[
                                         'Other Provider Identifier_2'],
                                     other_provider_identifier_type_code_2=row[
                                         'Other Provider Identifier Type Code_2'],
                                     other_provider_identifier_state_2=row[
                                         'Other Provider Identifier State_2'],
                                     other_provider_identifier_issuer_2=row[
                                         'Other Provider Identifier Issuer_2'],
                                     other_provider_identifier_3=row[
                                         'Other Provider Identifier_3'],
                                     other_provider_identifier_type_code_3=row[
                                         'Other Provider Identifier Type Code_3'],
                                     other_provider_identifier_state_3=row[
                                         'Other Provider Identifier State_3'],
                                     other_provider_identifier_issuer_3=row[
                                         'Other Provider Identifier Issuer_3'],
                                     other_provider_identifier_4=row[
                                         'Other Provider Identifier_4'],
                                     other_provider_identifier_type_code_4=row[
                                         'Other Provider Identifier Type Code_4'],
                                     other_provider_identifier_state_4=row[
                                         'Other Provider Identifier State_4'],
                                     other_provider_identifier_issuer_4=row[
                                         'Other Provider Identifier Issuer_4'],
                                     other_provider_identifier_5=row[
                                         'Other Provider Identifier_5'],
                                     other_provider_identifier_type_code_5=row[
                                         'Other Provider Identifier Type Code_5'],
                                     other_provider_identifier_state_5=row[
                                         'Other Provider Identifier State_5'],
                                     other_provider_identifier_issuer_5=row[
                                         'Other Provider Identifier Issuer_5'],
                                     other_provider_identifier_6=row[
                                         'Other Provider Identifier_6'],
                                     other_provider_identifier_type_code_6=row[
                                         'Other Provider Identifier Type Code_6'],
                                     other_provider_identifier_state_6=row[
                                         'Other Provider Identifier State_6'],
                                     other_provider_identifier_issuer_6=row[
                                         'Other Provider Identifier Issuer_6'],
                                     other_provider_identifier_7=row[
                                         'Other Provider Identifier_7'],
                                     other_provider_identifier_type_code_7=row[
                                         'Other Provider Identifier Type Code_7'],
                                     other_provider_identifier_state_7=row[
                                         'Other Provider Identifier State_7'],
                                     other_provider_identifier_issuer_7=row[
                                         'Other Provider Identifier Issuer_7'],
                                     other_provider_identifier_8=row[
                                         'Other Provider Identifier_8'],
                                     other_provider_identifier_type_code_8=row[
                                         'Other Provider Identifier Type Code_8'],
                                     other_provider_identifier_state_8=row[
                                         'Other Provider Identifier State_8'],
                                     other_provider_identifier_issuer_8=row[
                                         'Other Provider Identifier Issuer_8'],
                                     other_provider_identifier_9=row[
                                         'Other Provider Identifier_9'],
                                     other_provider_identifier_type_code_9=row[
                                         'Other Provider Identifier Type Code_9'],
                                     other_provider_identifier_state_9=row[
                                         'Other Provider Identifier State_9'],
                                     other_provider_identifier_issuer_9=row[
                                         'Other Provider Identifier Issuer_9'],
                                     other_provider_identifier_10=row[
                                         'Other Provider Identifier_10'],
                                     other_provider_identifier_type_code_10=row[
                                         'Other Provider Identifier Type Code_10'],
                                     other_provider_identifier_state_10=row[
                                         'Other Provider Identifier State_10'],
                                     other_provider_identifier_issuer_10=row[
                                         'Other Provider Identifier Issuer_10'],
                                     other_provider_identifier_11=row[
                                         'Other Provider Identifier_11'],
                                     other_provider_identifier_type_code_11=row[
                                         'Other Provider Identifier Type Code_11'],
                                     other_provider_identifier_state_11=row[
                                         'Other Provider Identifier State_11'],
                                     other_provider_identifier_issuer_11=row[
                                         'Other Provider Identifier Issuer_11'],
                                     other_provider_identifier_12=row[
                                         'Other Provider Identifier_12'],
                                     other_provider_identifier_type_code_12=row[
                                         'Other Provider Identifier Type Code_12'],
                                     other_provider_identifier_state_12=row[
                                         'Other Provider Identifier State_12'],
                                     other_provider_identifier_issuer_12=row[
                                         'Other Provider Identifier Issuer_12'],
                                     other_provider_identifier_13=row[
                                         'Other Provider Identifier_13'],
                                     other_provider_identifier_type_code_13=row[
                                         'Other Provider Identifier Type Code_13'],
                                     other_provider_identifier_state_13=row[
                                         'Other Provider Identifier State_13'],
                                     other_provider_identifier_issuer_13=row[
                                         'Other Provider Identifier Issuer_13'],
                                     other_provider_identifier_14=row[
                                         'Other Provider Identifier_14'],
                                     other_provider_identifier_type_code_14=row[
                                         'Other Provider Identifier Type Code_14'],
                                     other_provider_identifier_state_14=row[
                                         'Other Provider Identifier State_14'],
                                     other_provider_identifier_issuer_14=row[
                                         'Other Provider Identifier Issuer_14'],
                                     other_provider_identifier_15=row[
                                         'Other Provider Identifier_15'],
                                     other_provider_identifier_type_code_15=row[
                                         'Other Provider Identifier Type Code_15'],
                                     other_provider_identifier_state_15=row[
                                         'Other Provider Identifier State_15'],
                                     other_provider_identifier_issuer_15=row[
                                         'Other Provider Identifier Issuer_15'],
                                     other_provider_identifier_16=row[
                                         'Other Provider Identifier_16'],
                                     other_provider_identifier_type_code_16=row[
                                         'Other Provider Identifier Type Code_16'],
                                     other_provider_identifier_state_16=row[
                                         'Other Provider Identifier State_16'],
                                     other_provider_identifier_issuer_16=row[
                                         'Other Provider Identifier Issuer_16'],
                                     other_provider_identifier_17=row[
                                         'Other Provider Identifier_17'],
                                     other_provider_identifier_type_code_17=row[
                                         'Other Provider Identifier Type Code_17'],
                                     other_provider_identifier_state_17=row[
                                         'Other Provider Identifier State_17'],
                                     other_provider_identifier_issuer_17=row[
                                         'Other Provider Identifier Issuer_17'],
                                     other_provider_identifier_18=row[
                                         'Other Provider Identifier_18'],
                                     other_provider_identifier_type_code_18=row[
                                         'Other Provider Identifier Type Code_18'],
                                     other_provider_identifier_state_18=row[
                                         'Other Provider Identifier State_18'],
                                     other_provider_identifier_issuer_18=row[
                                         'Other Provider Identifier Issuer_18'],
                                     other_provider_identifier_19=row[
                                         'Other Provider Identifier_19'],
                                     other_provider_identifier_type_code_19=row[
                                         'Other Provider Identifier Type Code_19'],
                                     other_provider_identifier_state_19=row[
                                         'Other Provider Identifier State_19'],
                                     other_provider_identifier_issuer_19=row[
                                         'Other Provider Identifier Issuer_19'],
                                     other_provider_identifier_20=row[
                                         'Other Provider Identifier_20'],
                                     other_provider_identifier_type_code_20=row[
                                         'Other Provider Identifier Type Code_20'],
                                     other_provider_identifier_state_20=row[
                                         'Other Provider Identifier State_20'],
                                     other_provider_identifier_issuer_20=row[
                                         'Other Provider Identifier Issuer_20'],
                                     other_provider_identifier_21=row[
                                         'Other Provider Identifier_21'],
                                     other_provider_identifier_type_code_21=row[
                                         'Other Provider Identifier Type Code_21'],
                                     other_provider_identifier_state_21=row[
                                         'Other Provider Identifier State_21'],
                                     other_provider_identifier_issuer_21=row[
                                         'Other Provider Identifier Issuer_21'],
                                     other_provider_identifier_22=row[
                                         'Other Provider Identifier_22'],
                                     other_provider_identifier_type_code_22=row[
                                         'Other Provider Identifier Type Code_22'],
                                     other_provider_identifier_state_22=row[
                                         'Other Provider Identifier State_22'],
                                     other_provider_identifier_issuer_22=row[
                                         'Other Provider Identifier Issuer_22'],
                                     other_provider_identifier_23=row[
                                         'Other Provider Identifier_23'],
                                     other_provider_identifier_type_code_23=row[
                                         'Other Provider Identifier Type Code_23'],
                                     other_provider_identifier_state_23=row[
                                         'Other Provider Identifier State_23'],
                                     other_provider_identifier_issuer_23=row[
                                         'Other Provider Identifier Issuer_23'],
                                     other_provider_identifier_24=row[
                                         'Other Provider Identifier_24'],
                                     other_provider_identifier_type_code_24=row[
                                         'Other Provider Identifier Type Code_24'],
                                     other_provider_identifier_state_24=row[
                                         'Other Provider Identifier State_24'],
                                     other_provider_identifier_issuer_24=row[
                                         'Other Provider Identifier Issuer_24'],
                                     other_provider_identifier_25=row[
                                         'Other Provider Identifier_25'],
                                     other_provider_identifier_type_code_25=row[
                                         'Other Provider Identifier Type Code_25'],
                                     other_provider_identifier_state_25=row[
                                         'Other Provider Identifier State_25'],
                                     other_provider_identifier_issuer_25=row[
                                         'Other Provider Identifier Issuer_25'],
                                     other_provider_identifier_26=row[
                                         'Other Provider Identifier_26'],
                                     other_provider_identifier_type_code_26=row[
                                         'Other Provider Identifier Type Code_26'],
                                     other_provider_identifier_state_26=row[
                                         'Other Provider Identifier State_26'],
                                     other_provider_identifier_issuer_26=row[
                                         'Other Provider Identifier Issuer_26'],
                                     other_provider_identifier_27=row[
                                         'Other Provider Identifier_27'],
                                     other_provider_identifier_type_code_27=row[
                                         'Other Provider Identifier Type Code_27'],
                                     other_provider_identifier_state_27=row[
                                         'Other Provider Identifier State_27'],
                                     other_provider_identifier_issuer_27=row[
                                         'Other Provider Identifier Issuer_27'],
                                     other_provider_identifier_28=row[
                                         'Other Provider Identifier_28'],
                                     other_provider_identifier_type_code_28=row[
                                         'Other Provider Identifier Type Code_28'],
                                     other_provider_identifier_state_28=row[
                                         'Other Provider Identifier State_28'],
                                     other_provider_identifier_issuer_28=row[
                                         'Other Provider Identifier Issuer_28'],
                                     other_provider_identifier_29=row[
                                         'Other Provider Identifier_29'],
                                     other_provider_identifier_type_code_29=row[
                                         'Other Provider Identifier Type Code_29'],
                                     other_provider_identifier_state_29=row[
                                         'Other Provider Identifier State_29'],
                                     other_provider_identifier_issuer_29=row[
                                         'Other Provider Identifier Issuer_29'],
                                     other_provider_identifier_30=row[
                                         'Other Provider Identifier_30'],
                                     other_provider_identifier_type_code_30=row[
                                         'Other Provider Identifier Type Code_30'],
                                     other_provider_identifier_state_30=row[
                                         'Other Provider Identifier State_30'],
                                     other_provider_identifier_issuer_30=row[
                                         'Other Provider Identifier Issuer_30'],
                                     other_provider_identifier_31=row[
                                         'Other Provider Identifier_31'],
                                     other_provider_identifier_type_code_31=row[
                                         'Other Provider Identifier Type Code_31'],
                                     other_provider_identifier_state_31=row[
                                         'Other Provider Identifier State_31'],
                                     other_provider_identifier_issuer_31=row[
                                         'Other Provider Identifier Issuer_31'],
                                     other_provider_identifier_32=row[
                                         'Other Provider Identifier_32'],
                                     other_provider_identifier_type_code_32=row[
                                         'Other Provider Identifier Type Code_32'],
                                     other_provider_identifier_state_32=row[
                                         'Other Provider Identifier State_32'],
                                     other_provider_identifier_issuer_32=row[
                                         'Other Provider Identifier Issuer_32'],
                                     other_provider_identifier_33=row[
                                         'Other Provider Identifier_33'],
                                     other_provider_identifier_type_code_33=row[
                                         'Other Provider Identifier Type Code_33'],
                                     other_provider_identifier_state_33=row[
                                         'Other Provider Identifier State_33'],
                                     other_provider_identifier_issuer_33=row[
                                         'Other Provider Identifier Issuer_33'],
                                     other_provider_identifier_34=row[
                                         'Other Provider Identifier_34'],
                                     other_provider_identifier_type_code_34=row[
                                         'Other Provider Identifier Type Code_34'],
                                     other_provider_identifier_state_34=row[
                                         'Other Provider Identifier State_34'],
                                     other_provider_identifier_issuer_34=row[
                                         'Other Provider Identifier Issuer_34'],
                                     other_provider_identifier_35=row[
                                         'Other Provider Identifier_35'],
                                     other_provider_identifier_type_code_35=row[
                                         'Other Provider Identifier Type Code_35'],
                                     other_provider_identifier_state_35=row[
                                         'Other Provider Identifier State_35'],
                                     other_provider_identifier_issuer_35=row[
                                         'Other Provider Identifier Issuer_35'],
                                     other_provider_identifier_36=row[
                                         'Other Provider Identifier_36'],
                                     other_provider_identifier_type_code_36=row[
                                         'Other Provider Identifier Type Code_36'],
                                     other_provider_identifier_state_36=row[
                                         'Other Provider Identifier State_36'],
                                     other_provider_identifier_issuer_36=row[
                                         'Other Provider Identifier Issuer_36'],
                                     other_provider_identifier_37=row[
                                         'Other Provider Identifier_37'],
                                     other_provider_identifier_type_code_37=row[
                                         'Other Provider Identifier Type Code_37'],
                                     other_provider_identifier_state_37=row[
                                         'Other Provider Identifier State_37'],
                                     other_provider_identifier_issuer_37=row[
                                         'Other Provider Identifier Issuer_37'],
                                     other_provider_identifier_38=row[
                                         'Other Provider Identifier_38'],
                                     other_provider_identifier_type_code_38=row[
                                         'Other Provider Identifier Type Code_38'],
                                     other_provider_identifier_state_38=row[
                                         'Other Provider Identifier State_38'],
                                     other_provider_identifier_issuer_38=row[
                                         'Other Provider Identifier Issuer_38'],
                                     other_provider_identifier_39=row[
                                         'Other Provider Identifier_39'],
                                     other_provider_identifier_type_code_39=row[
                                         'Other Provider Identifier Type Code_39'],
                                     other_provider_identifier_state_39=row[
                                         'Other Provider Identifier State_39'],
                                     other_provider_identifier_issuer_39=row[
                                         'Other Provider Identifier Issuer_39'],
                                     other_provider_identifier_40=row[
                                         'Other Provider Identifier_40'],
                                     other_provider_identifier_type_code_40=row[
                                         'Other Provider Identifier Type Code_40'],
                                     other_provider_identifier_state_40=row[
                                         'Other Provider Identifier State_40'],
                                     other_provider_identifier_issuer_40=row[
                                         'Other Provider Identifier Issuer_40'],
                                     other_provider_identifier_41=row[
                                         'Other Provider Identifier_41'],
                                     other_provider_identifier_type_code_41=row[
                                         'Other Provider Identifier Type Code_41'],
                                     other_provider_identifier_state_41=row[
                                         'Other Provider Identifier State_41'],
                                     other_provider_identifier_issuer_41=row[
                                         'Other Provider Identifier Issuer_41'],
                                     other_provider_identifier_42=row[
                                         'Other Provider Identifier_42'],
                                     other_provider_identifier_type_code_42=row[
                                         'Other Provider Identifier Type Code_42'],
                                     other_provider_identifier_state_42=row[
                                         'Other Provider Identifier State_42'],
                                     other_provider_identifier_issuer_42=row[
                                         'Other Provider Identifier Issuer_42'],
                                     other_provider_identifier_43=row[
                                         'Other Provider Identifier_43'],
                                     other_provider_identifier_type_code_43=row[
                                         'Other Provider Identifier Type Code_43'],
                                     other_provider_identifier_state_43=row[
                                         'Other Provider Identifier State_43'],
                                     other_provider_identifier_issuer_43=row[
                                         'Other Provider Identifier Issuer_43'],
                                     other_provider_identifier_44=row[
                                         'Other Provider Identifier_44'],
                                     other_provider_identifier_type_code_44=row[
                                         'Other Provider Identifier Type Code_44'],
                                     other_provider_identifier_state_44=row[
                                         'Other Provider Identifier State_44'],
                                     other_provider_identifier_issuer_44=row[
                                         'Other Provider Identifier Issuer_44'],
                                     other_provider_identifier_45=row[
                                         'Other Provider Identifier_45'],
                                     other_provider_identifier_type_code_45=row[
                                         'Other Provider Identifier Type Code_45'],
                                     other_provider_identifier_state_45=row[
                                         'Other Provider Identifier State_45'],
                                     other_provider_identifier_issuer_45=row[
                                         'Other Provider Identifier Issuer_45'],
                                     other_provider_identifier_46=row[
                                         'Other Provider Identifier_46'],
                                     other_provider_identifier_type_code_46=row[
                                         'Other Provider Identifier Type Code_46'],
                                     other_provider_identifier_state_46=row[
                                         'Other Provider Identifier State_46'],
                                     other_provider_identifier_issuer_46=row[
                                         'Other Provider Identifier Issuer_46'],
                                     other_provider_identifier_47=row[
                                         'Other Provider Identifier_47'],
                                     other_provider_identifier_type_code_47=row[
                                         'Other Provider Identifier Type Code_47'],
                                     other_provider_identifier_state_47=row[
                                         'Other Provider Identifier State_47'],
                                     other_provider_identifier_issuer_47=row[
                                         'Other Provider Identifier Issuer_47'],
                                     other_provider_identifier_48=row[
                                         'Other Provider Identifier_48'],
                                     other_provider_identifier_type_code_48=row[
                                         'Other Provider Identifier Type Code_48'],
                                     other_provider_identifier_state_48=row[
                                         'Other Provider Identifier State_48'],
                                     other_provider_identifier_issuer_48=row[
                                         'Other Provider Identifier Issuer_48'],
                                     other_provider_identifier_49=row[
                                         'Other Provider Identifier_49'],
                                     other_provider_identifier_type_code_49=row[
                                         'Other Provider Identifier Type Code_49'],
                                     other_provider_identifier_state_49=row[
                                         'Other Provider Identifier State_49'],
                                     other_provider_identifier_issuer_49=row[
                                         'Other Provider Identifier Issuer_49'],
                                     other_provider_identifier_50=row[
                                         'Other Provider Identifier_50'],
                                     other_provider_identifier_type_code_50=row[
                                         'Other Provider Identifier Type Code_50'],
                                     other_provider_identifier_state_50=row[
                                         'Other Provider Identifier State_50'],
                                     other_provider_identifier_issuer_50=row[
                                         'Other Provider Identifier Issuer_50'],
                                     is_sole_proprietor=row['Is Sole Proprietor'],
                                     is_organization_subpart=row['Is Organization Subpart'],
                                     parent_organization_lbn=row['Parent Organization LBN'],
                                     parent_organization_tin=row['Parent Organization TIN'],
                                     authorized_official_name_prefix_text=row[
                                         'Authorized Official Name Prefix Text'],
                                     authorized_official_name_suffix_text=row[
                                         'Authorized Official Name Suffix Text'],
                                     authorized_official_credential_text=row[
                                         'Authorized Official Credential Text'],
                                     healthcare_provider_taxonomy_group_1=row[
                                         'Healthcare Provider Taxonomy Group_1'],
                                     healthcare_provider_taxonomy_group_2=row[
                                         'Healthcare Provider Taxonomy Group_2'],
                                     healthcare_provider_taxonomy_group_3=row[
                                         'Healthcare Provider Taxonomy Group_3'],
                                     healthcare_provider_taxonomy_group_4=row[
                                         'Healthcare Provider Taxonomy Group_4'],
                                     healthcare_provider_taxonomy_group_5=row[
                                         'Healthcare Provider Taxonomy Group_5'],
                                     healthcare_provider_taxonomy_group_6=row[
                                         'Healthcare Provider Taxonomy Group_6'],
                                     healthcare_provider_taxonomy_group_7=row[
                                         'Healthcare Provider Taxonomy Group_7'],
                                     healthcare_provider_taxonomy_group_8=row[
                                         'Healthcare Provider Taxonomy Group_8'],
                                     healthcare_provider_taxonomy_group_9=row[
                                         'Healthcare Provider Taxonomy Group_9'],
                                     healthcare_provider_taxonomy_group_10=row[
                                         'Healthcare Provider Taxonomy Group_10'],
                                     healthcare_provider_taxonomy_group_11=row[
                                         'Healthcare Provider Taxonomy Group_11'],
                                     healthcare_provider_taxonomy_group_12=row[
                                         'Healthcare Provider Taxonomy Group_12'],
                                     healthcare_provider_taxonomy_group_13=row[
                                         'Healthcare Provider Taxonomy Group_13'],
                                     healthcare_provider_taxonomy_group_14=row[
                                         'Healthcare Provider Taxonomy Group_14'],
                                     healthcare_provider_taxonomy_group_15=row[
                                         'Healthcare Provider Taxonomy Group_15'],
                                     certification_date=row['Certification Date']

                                     )
            db.session.add(db_npi)
            db.session.commit()
            key = row['NPI']
            data[key] = row

        buffer.close()
        file.file.close()
        return data

    except Exception:
        return Response("Internal server error", status_code=500)


@app.get("/api/v1/provider-search/")
def provider_npi_data(query: Optional[str] = None):
    if len(query.split()) == 1:
        search_query = db.session.query(
            NPIProviderData).filter(
            NPIProviderData.npi.contains(query.strip().upper())
        ).limit(20).all() or db.session.query(
            NPIProviderData).filter(
            NPIProviderData.provider_first_name.contains(query.strip().upper())
        ).limit(20).all() or db.session.query(
            NPIProviderData).filter(
            NPIProviderData.provider_middle_name.contains(query.strip().upper())
        ).limit(20).all()

        db.session.close()

        return search_query

    elif len(query.split()) > 1:
        spl = query.split()
        search_query = db.session.query(
            NPIProviderData).filter(and_(
            NPIProviderData.provider_first_name == spl[0].strip().upper(),
            NPIProviderData.provider_last_name_legal_name.startswith(spl[1].strip().upper())
        )).limit(20).all()

        db.session.close()
        return search_query

    else:
        return ""


@app.get("/api/v1/hospital-search/")
def hospital_npi_data(query: Optional[str]):
    if query:
        search_query = db.session.query(
            NPIHospitalData).filter(
            NPIHospitalData.npi.contains(query.upper())
        ).limit(20).all() or db.session.query(
            NPIHospitalData).filter(
            NPIHospitalData.provider_organization_name_legal_business_name.contains(query.upper())
        ).limit(20).all() or db.session.query(
            NPIHospitalData).filter(
            NPIHospitalData.provider_first_name.contains(query.upper())
        ).limit(20).all() or db.session.query(
            NPIHospitalData).filter(
            NPIHospitalData.provider_middle_name.contains(query.upper())
        ).limit(20).all()
        db.session.close()
        return search_query

    else:
        return ""


# @app.get("/api/v1/provider-search/", response_model=Page[SchemaNPIProviderData])
# def provider_npi_data(query: Optional[str] = None):
#     if query:
#         search_query = db.session.query(
#             NPIProviderData).filter(
#             NPIProviderData.npi.contains(query)
#         ).limit(10).all() or db.session.query(
#             NPIProviderData).filter(
#             NPIProviderData.provider_first_name.contains(query)
#         ).limit(10).all() or db.session.query(
#             NPIProviderData).filter(
#             NPIProviderData.provider_middle_name.contains(query)
#         ).limit(10).all()
#         db.session.close()
#         return paginate(search_query)
#     else:
#         return ""
#
#
# @app.get("/api/v1/hospital-search/", response_model=Page[SchemaNPIHospitalData])
# def hospital_npi_data(query: Optional[str]):
#     if query:
#         search_query = db.session.query(
#             NPIHospitalData).filter(
#             NPIHospitalData.npi.contains(query)
#         ).limit(10).all() or db.session.query(
#             NPIHospitalData).filter(
#             NPIHospitalData.provider_organization_name_legal_business_name.contains(query)
#         ).limit(10).all() or db.session.query(
#             NPIHospitalData).filter(
#             NPIHospitalData.provider_first_name.contains(query)
#         ).limit(10).all() or db.session.query(
#             NPIHospitalData).filter(
#             NPIHospitalData.provider_middle_name.contains(query)
#         ).limit(10).all()
#         db.session.close()
#         return paginate(search_query)
#
#     else:
#         return ""




# @app.get("/allhospitals/", response_model=list[schemas.NPIHospitalData])
# def read_npihospitals( db: Session = Depends(get_db)):
#     users = crud.get_users(db, )
#     return users

# @app.get("/allnpiproviders/", response_model=list[schemas.NPIProviderData])
# def read_providers( db: Session = Depends(get_db)):
#     providers = crud.get_users(db, )
#     return providers


# @app.get("/allnpidata/", response_model=list[schemas.NationalProviderIdentifier])
# def read_npidata( db: Session = Depends(get_db)):
#     providers = crud.get_users(db, )
#     return providers














if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)