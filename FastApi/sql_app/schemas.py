from pydantic import BaseModel

from datetime import datetime
from typing import Optional



class ItemBase(BaseModel):
    title: str
    description: str | None = None


class ItemCreate(ItemBase):
    pass


class Item(ItemBase):
    id: int
    owner_id: int

    class Config:
        orm_mode = True


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    is_active: bool
    items: list[Item] = []

    class Config:
        orm_mode = True
        
        


class NationalProviderIdentifier(BaseModel):
    npi_id: Optional[str]
    endpoint_type: Optional[str]
    endpoint_type_description: Optional[str]
    endpoint: Optional[str]
    affiliation: Optional[str]
    endpoint_description: Optional[str]
    affiliation_legal_business_name: Optional[str]
    use_code: Optional[str]
    use_description: Optional[str]
    other_use_description: Optional[str]
    content_type: Optional[str]
    content_description: Optional[str]
    other_content_description: Optional[str]
    affiliation_address_line_one: Optional[str]
    affiliation_address_line_two: Optional[str]
    affiliation_address_city: Optional[str]
    affiliation_address_state: Optional[str]
    affiliation_address_country: Optional[str]
    affiliation_address_postal_code: Optional[str]

    class Config:
        orm_mode = True


class NPIProviderData(BaseModel):
    npi: Optional[str]
    entity_type_code: Optional[str]
    replacement_npi: Optional[str]
    employer_identification_number_ein: Optional[str]
    provider_organization_name_legal_business_name: Optional[str]
    provider_last_name_legal_name: Optional[str]
    provider_first_name: Optional[str]
    provider_middle_name: Optional[str]
    provider_name_prefix_text: Optional[str]
    provider_name_suffix_text: Optional[str]
    provider_credential_text: Optional[str]
    provider_other_organization_name: Optional[str]
    provider_other_organization_name_type_code: Optional[str]
    provider_other_last_name: Optional[str]
    provider_other_first_name: Optional[str]
    provider_other_middle_name: Optional[str]
    provider_other_name_prefix_text: Optional[str]
    provider_other_name_suffix_text: Optional[str]
    provider_other_credential_text: Optional[str]
    provider_other_last_name_type_code: Optional[str]
    provider_first_line_business_mailing_address: Optional[str]
    provider_second_line_business_mailing_address: Optional[str]
    provider_business_mailing_address_city_name: Optional[str]
    provider_business_mailing_address_state_name: Optional[str]
    provider_business_mailing_address_postal_code: Optional[str]
    provider_business_mailing_address_country_code_if_outside_u_s: Optional[str]
    provider_business_mailing_address_telephone_number: Optional[str]
    provider_business_mailing_address_fax_number: Optional[str]
    provider_first_line_business_practice_location_address: Optional[str]
    provider_second_line_business_practice_location_address: Optional[str]
    provider_business_practice_location_address_city_name: Optional[str]
    provider_business_practice_location_address_state_name: Optional[str]
    provider_business_practice_location_address_postal_code: Optional[str]
    provider_business_practice_location_address_country_code_if_outside_u_s: Optional[str]
    provider_business_practice_location_address_telephone_number: Optional[str]
    provider_business_practice_location_address_fax_number: Optional[str]
    provider_enumeration_date: Optional[str]
    last_update_date: Optional[str]
    npi_deactivation_reason_code: Optional[str]
    npi_deactivation_date: Optional[str]
    npi_reactivation_date: Optional[str]
    provider_gender_code: Optional[str]
    authorized_official_last_name: Optional[str]
    authorized_official_first_name: Optional[str]
    authorized_official_middle_name: Optional[str]
    authorized_official_title_or_position: Optional[str]
    authorized_official_telephone_number: Optional[str]
    healthcare_provider_taxonomy_code_1: Optional[str]
    provider_license_number_1: Optional[str]
    provider_license_number_state_code_1: Optional[str]
    healthcare_provider_primary_taxonomy_switch_1: Optional[str]
    healthcare_provider_taxonomy_code_2: Optional[str]
    provider_license_number_2: Optional[str]
    provider_license_number_state_code_2: Optional[str]
    healthcare_provider_primary_taxonomy_switch_2: Optional[str]
    healthcare_provider_taxonomy_code_3: Optional[str]
    provider_license_number_3: Optional[str]
    provider_license_number_state_code_3: Optional[str]
    healthcare_provider_primary_taxonomy_switch_3: Optional[str]
    healthcare_provider_taxonomy_code_4: Optional[str]
    provider_license_number_4: Optional[str]
    provider_license_number_state_code_4: Optional[str]
    healthcare_provider_primary_taxonomy_switch_4: Optional[str]
    healthcare_provider_taxonomy_code_5: Optional[str]
    provider_license_number_5: Optional[str]
    provider_license_number_state_code_5: Optional[str]
    healthcare_provider_primary_taxonomy_switch_5: Optional[str]
    healthcare_provider_taxonomy_code_6: Optional[str]
    provider_license_number_6: Optional[str]
    provider_license_number_state_code_6: Optional[str]
    healthcare_provider_primary_taxonomy_switch_6: Optional[str]
    healthcare_provider_taxonomy_code_7: Optional[str]
    provider_license_number_7: Optional[str]
    provider_license_number_state_code_7: Optional[str]
    healthcare_provider_primary_taxonomy_switch_7: Optional[str]
    healthcare_provider_taxonomy_code_8: Optional[str]
    provider_license_number_8: Optional[str]
    provider_license_number_state_code_8: Optional[str]
    healthcare_provider_primary_taxonomy_switch_8: Optional[str]
    healthcare_provider_taxonomy_code_9: Optional[str]
    provider_license_number_9: Optional[str]
    provider_license_number_state_code_9: Optional[str]
    healthcare_provider_primary_taxonomy_switch_9: Optional[str]
    healthcare_provider_taxonomy_code_10: Optional[str]
    provider_license_number_10: Optional[str]
    provider_license_number_state_code_10: Optional[str]
    healthcare_provider_primary_taxonomy_switch_10: Optional[str]
    healthcare_provider_taxonomy_code_11: Optional[str]
    provider_license_number_11: Optional[str]
    provider_license_number_state_code_11: Optional[str]
    healthcare_provider_primary_taxonomy_switch_11: Optional[str]
    healthcare_provider_taxonomy_code_12: Optional[str]
    provider_license_number_12: Optional[str]
    provider_license_number_state_code_12: Optional[str]
    healthcare_provider_primary_taxonomy_switch_12: Optional[str]
    healthcare_provider_taxonomy_code_13: Optional[str]
    provider_license_number_13: Optional[str]
    provider_license_number_state_code_13: Optional[str]
    healthcare_provider_primary_taxonomy_switch_13: Optional[str]
    healthcare_provider_taxonomy_code_14: Optional[str]
    provider_license_number_14: Optional[str]
    provider_license_number_state_code_14: Optional[str]
    healthcare_provider_primary_taxonomy_switch_14: Optional[str]
    healthcare_provider_taxonomy_code_15: Optional[str]
    provider_license_number_15: Optional[str]
    provider_license_number_state_code_15: Optional[str]
    healthcare_provider_primary_taxonomy_switch_15: Optional[str]
    other_provider_identifier_1: Optional[str]
    other_provider_identifier_type_code_1: Optional[str]
    other_provider_identifier_state_1: Optional[str]
    other_provider_identifier_issuer_1: Optional[str]
    other_provider_identifier_2: Optional[str]
    other_provider_identifier_type_code_2: Optional[str]
    other_provider_identifier_state_2: Optional[str]
    other_provider_identifier_issuer_2: Optional[str]
    other_provider_identifier_3: Optional[str]
    other_provider_identifier_type_code_3: Optional[str]
    other_provider_identifier_state_3: Optional[str]
    other_provider_identifier_issuer_3: Optional[str]
    other_provider_identifier_4: Optional[str]
    other_provider_identifier_type_code_4: Optional[str]
    other_provider_identifier_state_4: Optional[str]
    other_provider_identifier_issuer_4: Optional[str]
    other_provider_identifier_5: Optional[str]
    other_provider_identifier_type_code_5: Optional[str]
    other_provider_identifier_state_5: Optional[str]
    other_provider_identifier_issuer_5: Optional[str]
    other_provider_identifier_6: Optional[str]
    other_provider_identifier_type_code_6: Optional[str]
    other_provider_identifier_state_6: Optional[str]
    other_provider_identifier_issuer_6: Optional[str]
    other_provider_identifier_7: Optional[str]
    other_provider_identifier_type_code_7: Optional[str]
    other_provider_identifier_state_7: Optional[str]
    other_provider_identifier_issuer_7: Optional[str]
    other_provider_identifier_8: Optional[str]
    other_provider_identifier_type_code_8: Optional[str]
    other_provider_identifier_state_8: Optional[str]
    other_provider_identifier_issuer_8: Optional[str]
    other_provider_identifier_9: Optional[str]
    other_provider_identifier_type_code_9: Optional[str]
    other_provider_identifier_state_9: Optional[str]
    other_provider_identifier_issuer_9: Optional[str]
    other_provider_identifier_10: Optional[str]
    other_provider_identifier_type_code_10: Optional[str]
    other_provider_identifier_state_10: Optional[str]
    other_provider_identifier_issuer_10: Optional[str]
    other_provider_identifier_11: Optional[str]
    other_provider_identifier_type_code_11: Optional[str]
    other_provider_identifier_state_11: Optional[str]
    other_provider_identifier_issuer_11: Optional[str]
    other_provider_identifier_12: Optional[str]
    other_provider_identifier_type_code_12: Optional[str]
    other_provider_identifier_state_12: Optional[str]
    other_provider_identifier_issuer_12: Optional[str]
    other_provider_identifier_13: Optional[str]
    other_provider_identifier_type_code_13: Optional[str]
    other_provider_identifier_state_13: Optional[str]
    other_provider_identifier_issuer_13: Optional[str]
    other_provider_identifier_14: Optional[str]
    other_provider_identifier_type_code_14: Optional[str]
    other_provider_identifier_state_14: Optional[str]
    other_provider_identifier_issuer_14: Optional[str]
    other_provider_identifier_15: Optional[str]
    other_provider_identifier_type_code_15: Optional[str]
    other_provider_identifier_state_15: Optional[str]
    other_provider_identifier_issuer_15: Optional[str]
    other_provider_identifier_16: Optional[str]
    other_provider_identifier_type_code_16: Optional[str]
    other_provider_identifier_state_16: Optional[str]
    other_provider_identifier_issuer_16: Optional[str]
    other_provider_identifier_17: Optional[str]
    other_provider_identifier_type_code_17: Optional[str]
    other_provider_identifier_state_17: Optional[str]
    other_provider_identifier_issuer_17: Optional[str]
    other_provider_identifier_18: Optional[str]
    other_provider_identifier_type_code_18: Optional[str]
    other_provider_identifier_state_18: Optional[str]
    other_provider_identifier_issuer_18: Optional[str]
    other_provider_identifier_19: Optional[str]
    other_provider_identifier_type_code_19: Optional[str]
    other_provider_identifier_state_19: Optional[str]
    other_provider_identifier_issuer_19: Optional[str]
    other_provider_identifier_20: Optional[str]
    other_provider_identifier_type_code_20: Optional[str]
    other_provider_identifier_state_20: Optional[str]
    other_provider_identifier_issuer_20: Optional[str]
    other_provider_identifier_21: Optional[str]
    other_provider_identifier_type_code_21: Optional[str]
    other_provider_identifier_state_21: Optional[str]
    other_provider_identifier_issuer_21: Optional[str]
    other_provider_identifier_22: Optional[str]
    other_provider_identifier_type_code_22: Optional[str]
    other_provider_identifier_state_22: Optional[str]
    other_provider_identifier_issuer_22: Optional[str]
    other_provider_identifier_23: Optional[str]
    other_provider_identifier_type_code_23: Optional[str]
    other_provider_identifier_state_23: Optional[str]
    other_provider_identifier_issuer_23: Optional[str]
    other_provider_identifier_24: Optional[str]
    other_provider_identifier_type_code_24: Optional[str]
    other_provider_identifier_state_24: Optional[str]
    other_provider_identifier_issuer_24: Optional[str]
    other_provider_identifier_25: Optional[str]
    other_provider_identifier_type_code_25: Optional[str]
    other_provider_identifier_state_25: Optional[str]
    other_provider_identifier_issuer_25: Optional[str]
    other_provider_identifier_26: Optional[str]
    other_provider_identifier_type_code_26: Optional[str]
    other_provider_identifier_state_26: Optional[str]
    other_provider_identifier_issuer_26: Optional[str]
    other_provider_identifier_27: Optional[str]
    other_provider_identifier_type_code_27: Optional[str]
    other_provider_identifier_state_27: Optional[str]
    other_provider_identifier_issuer_27: Optional[str]
    other_provider_identifier_28: Optional[str]
    other_provider_identifier_type_code_28: Optional[str]
    other_provider_identifier_state_28: Optional[str]
    other_provider_identifier_issuer_28: Optional[str]
    other_provider_identifier_29: Optional[str]
    other_provider_identifier_type_code_29: Optional[str]
    other_provider_identifier_state_29: Optional[str]
    other_provider_identifier_issuer_29: Optional[str]
    other_provider_identifier_30: Optional[str]
    other_provider_identifier_type_code_30: Optional[str]
    other_provider_identifier_state_30: Optional[str]
    other_provider_identifier_issuer_30: Optional[str]
    other_provider_identifier_31: Optional[str]
    other_provider_identifier_type_code_31: Optional[str]
    other_provider_identifier_state_31: Optional[str]
    other_provider_identifier_issuer_31: Optional[str]
    other_provider_identifier_32: Optional[str]
    other_provider_identifier_type_code_32: Optional[str]
    other_provider_identifier_state_32: Optional[str]
    other_provider_identifier_issuer_32: Optional[str]
    other_provider_identifier_33: Optional[str]
    other_provider_identifier_type_code_33: Optional[str]
    other_provider_identifier_state_33: Optional[str]
    other_provider_identifier_issuer_33: Optional[str]
    other_provider_identifier_34: Optional[str]
    other_provider_identifier_type_code_34: Optional[str]
    other_provider_identifier_state_34: Optional[str]
    other_provider_identifier_issuer_34: Optional[str]
    other_provider_identifier_35: Optional[str]
    other_provider_identifier_type_code_35: Optional[str]
    other_provider_identifier_state_35: Optional[str]
    other_provider_identifier_issuer_35: Optional[str]
    other_provider_identifier_36: Optional[str]
    other_provider_identifier_type_code_36: Optional[str]
    other_provider_identifier_state_36: Optional[str]
    other_provider_identifier_issuer_36: Optional[str]
    other_provider_identifier_37: Optional[str]
    other_provider_identifier_type_code_37: Optional[str]
    other_provider_identifier_state_37: Optional[str]
    other_provider_identifier_issuer_37: Optional[str]
    other_provider_identifier_38: Optional[str]
    other_provider_identifier_type_code_38: Optional[str]
    other_provider_identifier_state_38: Optional[str]
    other_provider_identifier_issuer_38: Optional[str]
    other_provider_identifier_39: Optional[str]
    other_provider_identifier_type_code_39: Optional[str]
    other_provider_identifier_state_39: Optional[str]
    other_provider_identifier_issuer_39: Optional[str]
    other_provider_identifier_40: Optional[str]
    other_provider_identifier_type_code_40: Optional[str]
    other_provider_identifier_state_40: Optional[str]
    other_provider_identifier_issuer_40: Optional[str]
    other_provider_identifier_41: Optional[str]
    other_provider_identifier_type_code_41: Optional[str]
    other_provider_identifier_state_41: Optional[str]
    other_provider_identifier_issuer_41: Optional[str]
    other_provider_identifier_42: Optional[str]
    other_provider_identifier_type_code_42: Optional[str]
    other_provider_identifier_state_42: Optional[str]
    other_provider_identifier_issuer_42: Optional[str]
    other_provider_identifier_43: Optional[str]
    other_provider_identifier_type_code_43: Optional[str]
    other_provider_identifier_state_43: Optional[str]
    other_provider_identifier_issuer_43: Optional[str]
    other_provider_identifier_44: Optional[str]
    other_provider_identifier_type_code_44: Optional[str]
    other_provider_identifier_state_44: Optional[str]
    other_provider_identifier_issuer_44: Optional[str]
    other_provider_identifier_45: Optional[str]
    other_provider_identifier_type_code_45: Optional[str]
    other_provider_identifier_state_45: Optional[str]
    other_provider_identifier_issuer_45: Optional[str]
    other_provider_identifier_46: Optional[str]
    other_provider_identifier_type_code_46: Optional[str]
    other_provider_identifier_state_46: Optional[str]
    other_provider_identifier_issuer_46: Optional[str]
    other_provider_identifier_47: Optional[str]
    other_provider_identifier_type_code_47: Optional[str]
    other_provider_identifier_state_47: Optional[str]
    other_provider_identifier_issuer_47: Optional[str]
    other_provider_identifier_48: Optional[str]
    other_provider_identifier_type_code_48: Optional[str]
    other_provider_identifier_state_48: Optional[str]
    other_provider_identifier_issuer_48: Optional[str]
    other_provider_identifier_49: Optional[str]
    other_provider_identifier_type_code_49: Optional[str]
    other_provider_identifier_state_49: Optional[str]
    other_provider_identifier_issuer_49: Optional[str]
    other_provider_identifier_50: Optional[str]
    other_provider_identifier_type_code_50: Optional[str]
    other_provider_identifier_state_50: Optional[str]
    other_provider_identifier_issuer_50: Optional[str]
    is_sole_proprietor: Optional[str]
    is_organization_subpart: Optional[str]
    parent_organization_lbn: Optional[str]
    parent_organization_tin: Optional[str]
    authorized_official_name_prefix_text: Optional[str]
    authorized_official_name_suffix_text: Optional[str]
    authorized_official_credential_text: Optional[str]
    healthcare_provider_taxonomy_group_1: Optional[str]
    healthcare_provider_taxonomy_group_2: Optional[str]
    healthcare_provider_taxonomy_group_3: Optional[str]
    healthcare_provider_taxonomy_group_4: Optional[str]
    healthcare_provider_taxonomy_group_5: Optional[str]
    healthcare_provider_taxonomy_group_6: Optional[str]
    healthcare_provider_taxonomy_group_7: Optional[str]
    healthcare_provider_taxonomy_group_8: Optional[str]
    healthcare_provider_taxonomy_group_9: Optional[str]
    healthcare_provider_taxonomy_group_10: Optional[str]
    healthcare_provider_taxonomy_group_11: Optional[str]
    healthcare_provider_taxonomy_group_12: Optional[str]
    healthcare_provider_taxonomy_group_13: Optional[str]
    healthcare_provider_taxonomy_group_14: Optional[str]
    healthcare_provider_taxonomy_group_15: Optional[str]
    certification_date: Optional[str]

    class Config:
        orm_mode = True


class NPIHospitalData(BaseModel):
    npi: Optional[str]
    entity_type_code: Optional[str]
    replacement_npi: Optional[str]
    employer_identification_number_ein: Optional[str]
    provider_organization_name_legal_business_name: Optional[str]
    provider_last_name_legal_name: Optional[str]
    provider_first_name: Optional[str]
    provider_middle_name: Optional[str]
    provider_name_prefix_text: Optional[str]
    provider_name_suffix_text: Optional[str]
    provider_credential_text: Optional[str]
    provider_other_organization_name: Optional[str]
    provider_other_organization_name_type_code: Optional[str]
    provider_other_last_name: Optional[str]
    provider_other_first_name: Optional[str]
    provider_other_middle_name: Optional[str]
    provider_other_name_prefix_text: Optional[str]
    provider_other_name_suffix_text: Optional[str]
    provider_other_credential_text: Optional[str]
    provider_other_last_name_type_code: Optional[str]
    provider_first_line_business_mailing_address: Optional[str]
    provider_second_line_business_mailing_address: Optional[str]
    provider_business_mailing_address_city_name: Optional[str]
    provider_business_mailing_address_state_name: Optional[str]
    provider_business_mailing_address_postal_code: Optional[str]
    provider_business_mailing_address_country_code_if_outside_u_s: Optional[str]
    provider_business_mailing_address_telephone_number: Optional[str]
    provider_business_mailing_address_fax_number: Optional[str]
    provider_first_line_business_practice_location_address: Optional[str]
    provider_second_line_business_practice_location_address: Optional[str]
    provider_business_practice_location_address_city_name: Optional[str]
    provider_business_practice_location_address_state_name: Optional[str]
    provider_business_practice_location_address_postal_code: Optional[str]
    provider_business_practice_location_address_country_code_if_outside_u_s: Optional[str]
    provider_business_practice_location_address_telephone_number: Optional[str]
    provider_business_practice_location_address_fax_number: Optional[str]
    provider_enumeration_date: Optional[str]
    last_update_date: Optional[str]
    npi_deactivation_reason_code: Optional[str]
    npi_deactivation_date: Optional[str]
    npi_reactivation_date: Optional[str]
    provider_gender_code: Optional[str]
    authorized_official_last_name: Optional[str]
    authorized_official_first_name: Optional[str]
    authorized_official_middle_name: Optional[str]
    authorized_official_title_or_position: Optional[str]
    authorized_official_telephone_number: Optional[str]
    healthcare_provider_taxonomy_code_1: Optional[str]
    provider_license_number_1: Optional[str]
    provider_license_number_state_code_1: Optional[str]
    healthcare_provider_primary_taxonomy_switch_1: Optional[str]
    healthcare_provider_taxonomy_code_2: Optional[str]
    provider_license_number_2: Optional[str]
    provider_license_number_state_code_2: Optional[str]
    healthcare_provider_primary_taxonomy_switch_2: Optional[str]
    healthcare_provider_taxonomy_code_3: Optional[str]
    provider_license_number_3: Optional[str]
    provider_license_number_state_code_3: Optional[str]
    healthcare_provider_primary_taxonomy_switch_3: Optional[str]
    healthcare_provider_taxonomy_code_4: Optional[str]
    provider_license_number_4: Optional[str]
    provider_license_number_state_code_4: Optional[str]
    healthcare_provider_primary_taxonomy_switch_4: Optional[str]
    healthcare_provider_taxonomy_code_5: Optional[str]
    provider_license_number_5: Optional[str]
    provider_license_number_state_code_5: Optional[str]
    healthcare_provider_primary_taxonomy_switch_5: Optional[str]
    healthcare_provider_taxonomy_code_6: Optional[str]
    provider_license_number_6: Optional[str]
    provider_license_number_state_code_6: Optional[str]
    healthcare_provider_primary_taxonomy_switch_6: Optional[str]
    healthcare_provider_taxonomy_code_7: Optional[str]
    provider_license_number_7: Optional[str]
    provider_license_number_state_code_7: Optional[str]
    healthcare_provider_primary_taxonomy_switch_7: Optional[str]
    healthcare_provider_taxonomy_code_8: Optional[str]
    provider_license_number_8: Optional[str]
    provider_license_number_state_code_8: Optional[str]
    healthcare_provider_primary_taxonomy_switch_8: Optional[str]
    healthcare_provider_taxonomy_code_9: Optional[str]
    provider_license_number_9: Optional[str]
    provider_license_number_state_code_9: Optional[str]
    healthcare_provider_primary_taxonomy_switch_9: Optional[str]
    healthcare_provider_taxonomy_code_10: Optional[str]
    provider_license_number_10: Optional[str]
    provider_license_number_state_code_10: Optional[str]
    healthcare_provider_primary_taxonomy_switch_10: Optional[str]
    healthcare_provider_taxonomy_code_11: Optional[str]
    provider_license_number_11: Optional[str]
    provider_license_number_state_code_11: Optional[str]
    healthcare_provider_primary_taxonomy_switch_11: Optional[str]
    healthcare_provider_taxonomy_code_12: Optional[str]
    provider_license_number_12: Optional[str]
    provider_license_number_state_code_12: Optional[str]
    healthcare_provider_primary_taxonomy_switch_12: Optional[str]
    healthcare_provider_taxonomy_code_13: Optional[str]
    provider_license_number_13: Optional[str]
    provider_license_number_state_code_13: Optional[str]
    healthcare_provider_primary_taxonomy_switch_13: Optional[str]
    healthcare_provider_taxonomy_code_14: Optional[str]
    provider_license_number_14: Optional[str]
    provider_license_number_state_code_14: Optional[str]
    healthcare_provider_primary_taxonomy_switch_14: Optional[str]
    healthcare_provider_taxonomy_code_15: Optional[str]
    provider_license_number_15: Optional[str]
    provider_license_number_state_code_15: Optional[str]
    healthcare_provider_primary_taxonomy_switch_15: Optional[str]
    other_provider_identifier_1: Optional[str]
    other_provider_identifier_type_code_1: Optional[str]
    other_provider_identifier_state_1: Optional[str]
    other_provider_identifier_issuer_1: Optional[str]
    other_provider_identifier_2: Optional[str]
    other_provider_identifier_type_code_2: Optional[str]
    other_provider_identifier_state_2: Optional[str]
    other_provider_identifier_issuer_2: Optional[str]
    other_provider_identifier_3: Optional[str]
    other_provider_identifier_type_code_3: Optional[str]
    other_provider_identifier_state_3: Optional[str]
    other_provider_identifier_issuer_3: Optional[str]
    other_provider_identifier_4: Optional[str]
    other_provider_identifier_type_code_4: Optional[str]
    other_provider_identifier_state_4: Optional[str]
    other_provider_identifier_issuer_4: Optional[str]
    other_provider_identifier_5: Optional[str]
    other_provider_identifier_type_code_5: Optional[str]
    other_provider_identifier_state_5: Optional[str]
    other_provider_identifier_issuer_5: Optional[str]
    other_provider_identifier_6: Optional[str]
    other_provider_identifier_type_code_6: Optional[str]
    other_provider_identifier_state_6: Optional[str]
    other_provider_identifier_issuer_6: Optional[str]
    other_provider_identifier_7: Optional[str]
    other_provider_identifier_type_code_7: Optional[str]
    other_provider_identifier_state_7: Optional[str]
    other_provider_identifier_issuer_7: Optional[str]
    other_provider_identifier_8: Optional[str]
    other_provider_identifier_type_code_8: Optional[str]
    other_provider_identifier_state_8: Optional[str]
    other_provider_identifier_issuer_8: Optional[str]
    other_provider_identifier_9: Optional[str]
    other_provider_identifier_type_code_9: Optional[str]
    other_provider_identifier_state_9: Optional[str]
    other_provider_identifier_issuer_9: Optional[str]
    other_provider_identifier_10: Optional[str]
    other_provider_identifier_type_code_10: Optional[str]
    other_provider_identifier_state_10: Optional[str]
    other_provider_identifier_issuer_10: Optional[str]
    other_provider_identifier_11: Optional[str]
    other_provider_identifier_type_code_11: Optional[str]
    other_provider_identifier_state_11: Optional[str]
    other_provider_identifier_issuer_11: Optional[str]
    other_provider_identifier_12: Optional[str]
    other_provider_identifier_type_code_12: Optional[str]
    other_provider_identifier_state_12: Optional[str]
    other_provider_identifier_issuer_12: Optional[str]
    other_provider_identifier_13: Optional[str]
    other_provider_identifier_type_code_13: Optional[str]
    other_provider_identifier_state_13: Optional[str]
    other_provider_identifier_issuer_13: Optional[str]
    other_provider_identifier_14: Optional[str]
    other_provider_identifier_type_code_14: Optional[str]
    other_provider_identifier_state_14: Optional[str]
    other_provider_identifier_issuer_14: Optional[str]
    other_provider_identifier_15: Optional[str]
    other_provider_identifier_type_code_15: Optional[str]
    other_provider_identifier_state_15: Optional[str]
    other_provider_identifier_issuer_15: Optional[str]
    other_provider_identifier_16: Optional[str]
    other_provider_identifier_type_code_16: Optional[str]
    other_provider_identifier_state_16: Optional[str]
    other_provider_identifier_issuer_16: Optional[str]
    other_provider_identifier_17: Optional[str]
    other_provider_identifier_type_code_17: Optional[str]
    other_provider_identifier_state_17: Optional[str]
    other_provider_identifier_issuer_17: Optional[str]
    other_provider_identifier_18: Optional[str]
    other_provider_identifier_type_code_18: Optional[str]
    other_provider_identifier_state_18: Optional[str]
    other_provider_identifier_issuer_18: Optional[str]
    other_provider_identifier_19: Optional[str]
    other_provider_identifier_type_code_19: Optional[str]
    other_provider_identifier_state_19: Optional[str]
    other_provider_identifier_issuer_19: Optional[str]
    other_provider_identifier_20: Optional[str]
    other_provider_identifier_type_code_20: Optional[str]
    other_provider_identifier_state_20: Optional[str]
    other_provider_identifier_issuer_20: Optional[str]
    other_provider_identifier_21: Optional[str]
    other_provider_identifier_type_code_21: Optional[str]
    other_provider_identifier_state_21: Optional[str]
    other_provider_identifier_issuer_21: Optional[str]
    other_provider_identifier_22: Optional[str]
    other_provider_identifier_type_code_22: Optional[str]
    other_provider_identifier_state_22: Optional[str]
    other_provider_identifier_issuer_22: Optional[str]
    other_provider_identifier_23: Optional[str]
    other_provider_identifier_type_code_23: Optional[str]
    other_provider_identifier_state_23: Optional[str]
    other_provider_identifier_issuer_23: Optional[str]
    other_provider_identifier_24: Optional[str]
    other_provider_identifier_type_code_24: Optional[str]
    other_provider_identifier_state_24: Optional[str]
    other_provider_identifier_issuer_24: Optional[str]
    other_provider_identifier_25: Optional[str]
    other_provider_identifier_type_code_25: Optional[str]
    other_provider_identifier_state_25: Optional[str]
    other_provider_identifier_issuer_25: Optional[str]
    other_provider_identifier_26: Optional[str]
    other_provider_identifier_type_code_26: Optional[str]
    other_provider_identifier_state_26: Optional[str]
    other_provider_identifier_issuer_26: Optional[str]
    other_provider_identifier_27: Optional[str]
    other_provider_identifier_type_code_27: Optional[str]
    other_provider_identifier_state_27: Optional[str]
    other_provider_identifier_issuer_27: Optional[str]
    other_provider_identifier_28: Optional[str]
    other_provider_identifier_type_code_28: Optional[str]
    other_provider_identifier_state_28: Optional[str]
    other_provider_identifier_issuer_28: Optional[str]
    other_provider_identifier_29: Optional[str]
    other_provider_identifier_type_code_29: Optional[str]
    other_provider_identifier_state_29: Optional[str]
    other_provider_identifier_issuer_29: Optional[str]
    other_provider_identifier_30: Optional[str]
    other_provider_identifier_type_code_30: Optional[str]
    other_provider_identifier_state_30: Optional[str]
    other_provider_identifier_issuer_30: Optional[str]
    other_provider_identifier_31: Optional[str]
    other_provider_identifier_type_code_31: Optional[str]
    other_provider_identifier_state_31: Optional[str]
    other_provider_identifier_issuer_31: Optional[str]
    other_provider_identifier_32: Optional[str]
    other_provider_identifier_type_code_32: Optional[str]
    other_provider_identifier_state_32: Optional[str]
    other_provider_identifier_issuer_32: Optional[str]
    other_provider_identifier_33: Optional[str]
    other_provider_identifier_type_code_33: Optional[str]
    other_provider_identifier_state_33: Optional[str]
    other_provider_identifier_issuer_33: Optional[str]
    other_provider_identifier_34: Optional[str]
    other_provider_identifier_type_code_34: Optional[str]
    other_provider_identifier_state_34: Optional[str]
    other_provider_identifier_issuer_34: Optional[str]
    other_provider_identifier_35: Optional[str]
    other_provider_identifier_type_code_35: Optional[str]
    other_provider_identifier_state_35: Optional[str]
    other_provider_identifier_issuer_35: Optional[str]
    other_provider_identifier_36: Optional[str]
    other_provider_identifier_type_code_36: Optional[str]
    other_provider_identifier_state_36: Optional[str]
    other_provider_identifier_issuer_36: Optional[str]
    other_provider_identifier_37: Optional[str]
    other_provider_identifier_type_code_37: Optional[str]
    other_provider_identifier_state_37: Optional[str]
    other_provider_identifier_issuer_37: Optional[str]
    other_provider_identifier_38: Optional[str]
    other_provider_identifier_type_code_38: Optional[str]
    other_provider_identifier_state_38: Optional[str]
    other_provider_identifier_issuer_38: Optional[str]
    other_provider_identifier_39: Optional[str]
    other_provider_identifier_type_code_39: Optional[str]
    other_provider_identifier_state_39: Optional[str]
    other_provider_identifier_issuer_39: Optional[str]
    other_provider_identifier_40: Optional[str]
    other_provider_identifier_type_code_40: Optional[str]
    other_provider_identifier_state_40: Optional[str]
    other_provider_identifier_issuer_40: Optional[str]
    other_provider_identifier_41: Optional[str]
    other_provider_identifier_type_code_41: Optional[str]
    other_provider_identifier_state_41: Optional[str]
    other_provider_identifier_issuer_41: Optional[str]
    other_provider_identifier_42: Optional[str]
    other_provider_identifier_type_code_42: Optional[str]
    other_provider_identifier_state_42: Optional[str]
    other_provider_identifier_issuer_42: Optional[str]
    other_provider_identifier_43: Optional[str]
    other_provider_identifier_type_code_43: Optional[str]
    other_provider_identifier_state_43: Optional[str]
    other_provider_identifier_issuer_43: Optional[str]
    other_provider_identifier_44: Optional[str]
    other_provider_identifier_type_code_44: Optional[str]
    other_provider_identifier_state_44: Optional[str]
    other_provider_identifier_issuer_44: Optional[str]
    other_provider_identifier_45: Optional[str]
    other_provider_identifier_type_code_45: Optional[str]
    other_provider_identifier_state_45: Optional[str]
    other_provider_identifier_issuer_45: Optional[str]
    other_provider_identifier_46: Optional[str]
    other_provider_identifier_type_code_46: Optional[str]
    other_provider_identifier_state_46: Optional[str]
    other_provider_identifier_issuer_46: Optional[str]
    other_provider_identifier_47: Optional[str]
    other_provider_identifier_type_code_47: Optional[str]
    other_provider_identifier_state_47: Optional[str]
    other_provider_identifier_issuer_47: Optional[str]
    other_provider_identifier_48: Optional[str]
    other_provider_identifier_type_code_48: Optional[str]
    other_provider_identifier_state_48: Optional[str]
    other_provider_identifier_issuer_48: Optional[str]
    other_provider_identifier_49: Optional[str]
    other_provider_identifier_type_code_49: Optional[str]
    other_provider_identifier_state_49: Optional[str]
    other_provider_identifier_issuer_49: Optional[str]
    other_provider_identifier_50: Optional[str]
    other_provider_identifier_type_code_50: Optional[str]
    other_provider_identifier_state_50: Optional[str]
    other_provider_identifier_issuer_50: Optional[str]
    is_sole_proprietor: Optional[str]
    is_organization_subpart: Optional[str]
    parent_organization_lbn: Optional[str]
    parent_organization_tin: Optional[str]
    authorized_official_name_prefix_text: Optional[str]
    authorized_official_name_suffix_text: Optional[str]
    authorized_official_credential_text: Optional[str]
    healthcare_provider_taxonomy_group_1: Optional[str]
    healthcare_provider_taxonomy_group_2: Optional[str]
    healthcare_provider_taxonomy_group_3: Optional[str]
    healthcare_provider_taxonomy_group_4: Optional[str]
    healthcare_provider_taxonomy_group_5: Optional[str]
    healthcare_provider_taxonomy_group_6: Optional[str]
    healthcare_provider_taxonomy_group_7: Optional[str]
    healthcare_provider_taxonomy_group_8: Optional[str]
    healthcare_provider_taxonomy_group_9: Optional[str]
    healthcare_provider_taxonomy_group_10: Optional[str]
    healthcare_provider_taxonomy_group_11: Optional[str]
    healthcare_provider_taxonomy_group_12: Optional[str]
    healthcare_provider_taxonomy_group_13: Optional[str]
    healthcare_provider_taxonomy_group_14: Optional[str]
    healthcare_provider_taxonomy_group_15: Optional[str]
    certification_date: Optional[str]

    class Config:
        orm_mode = True