import requests
base_url = "https://practice-react.sdetunicorns.com/api/test/"
endpoint = "brands"
url = base_url + endpoint




# validate that the API successfully returns a list of brands.
print("validate that the API successfully returns a list of brands")
print('<br>')
Get_Brands_Req = requests.get(url)
Get_Brands_Res = Get_Brands_Req.json()
if Get_Brands_Req.status_code == 200:
    print("Status code for get brands is 200: success")
    print('<br>')
    # check that the list of brands has more than one entry.
    if (len(Get_Brands_Res) > 1):
        print("List of brands has more than one entry")
        print('<br>')
        flag_all_valid=1
	# validate that each brand object contains _id and name properties
        for brand in Get_Brands_Res:
            if '_id' not in brand or 'name' not in brand:
                print(f"Brand validation failed for: {brand}")
                print('<br>')
                flag_all_valid = 0
            else:
                pass
        if (flag_all_valid == 1):
            print("Each brand object contains _id and name properties")
            print('<br>')
        else:
            print("Not every brand object contains _id and name properties")
            print('<br>')
    else:
        print("List of brands has one entery or less")
        print('<br>')
else:
    print("status code is 422: cannot get brands")
    print('<br>')

# New lines separation for HTML report formating.
print('<br>')
print('<br>')
print('<br>')



# validate that a brand is successfully returned by a specific ID
print("validate that a brand is successfully returned by a specific ID")
print('<br>')
print("\n")
Specific_ID = "/6440965fbf61a969820eb749"
Expected_Brand_Name = "HE-MAN"
Specific_ID_Get_URL = url + Specific_ID
Get_Specific_ID_Req = requests.get(Specific_ID_Get_URL)
Get_Specific_ID_Res = Get_Specific_ID_Req.json()
if Get_Specific_ID_Req.status_code == 200:
    print("Status code is 200 success for ID: ", Specific_ID)
    print('<br>')
    Brand_Name = Get_Specific_ID_Res.get('name')
    # check that the brand's name matches the expected value
    if (Brand_Name == Expected_Brand_Name):
        print("Brand name of id: " +Specific_ID+ "is correct")
        print('<br>')
    else:
        print("Brand name of id: " +Specific_ID+ " is wrong")
        print('<br>')
else:
    print("Status code is not 200 success for ID: ", Specific_ID)
    print('<br>')

print('<br>')
print('<br>')
print('<br>')


# Validate that the API prevents the creation of duplicate brand entries
print("Validate that the API prevents the creation of duplicate brand entries")
print('<br>')
print("\n")
Post_Body = {'name': 'HE-MAN', 'description': 'Any'}
Post_Request = requests.post(url, json = Post_Body)
Post_Response= Post_Request.json()
if Post_Request.status_code == 200:
    print(Post_Response)
    print('<br>')
    print("New Brand Added")
    print('<br>')
else:
    print(Post_Response)
    print('<br>')



print('<br>')
print('<br>')
print('<br>')


# Validate that the API returns an appropriate error when attempting to retrieve a brand that does not exist via the GET /brands/:id request.
print("Validate that the API returns an appropriate error when attempting to retrieve a brand that does not exist via the GET /brands/:id request")
print('<br>')
print("\n")
Non_existent_id = "/6440965fbf61a969820eb749QQQQQQQAAAAAA"
Non_existent_brand = url + Non_existent_id
Non_existent_Req = requests.get(Non_existent_brand)
Non_existent_Res = Non_existent_Req.json()
Err_Desc = Non_existent_Res.get('error')
if (Err_Desc == 'Unable to fetch brand') or (Non_existent_Req.status_code != 200):
    print("Appropriate error, Brand with ID:" +Non_existent_id+ " does not exist")
    print('<br>')
elif (Non_existent_Req.status_code == 200):
    print("Brand with ID:" +Non_existent_id+ " exists")
    print('<br>')
else:
    print(Err_Desc)
    print('<br>')



print('<br>')
print('<br>')
print('<br>')


# Validate that the API throws an error when attempting to delete a non-existent brand.
print("Validate that the API throws an error when attempting to delete a non-existent brand")
print('<br>')
print("\n")
Delete_ID = "/6440965fbf61a969820ivQQQ89ojn3jA"
Delete_URL = url + Delete_ID
Delete_Req = requests.delete(Delete_URL)
Delete_Res = Delete_Req.json()
Del_Err_Desc = Delete_Res.get('error')
if (Del_Err_Desc == 'Unable to delete brand') or (Delete_Req.status_code != 200):
    print("Cannot fulfill delete request with ID:" +Delete_ID+ " ,Brand does not exist")
    print('<br>')
elif (Delete_Req.status_code == 200):
    print("Brand with ID:" +Delete_ID+ " deleted")
    print('<br>')
else:
    print(Del_Err_Desc)
    print('<br>')



print('<br>')
print('<br>')
print('<br>')


# Validate that the API throws an error when attempting to update a non-existent brand.
print("Validate that the API throws an error when attempting to update a non-existent brand")
print('<br>')
print("\n")
Update_ID = "/6440965ufnfidcr6ndl820ivQQQ89ojn3jA"
Update_URL = url + Update_ID
put_body = {'name': 'SHE-MAN', 'description': 'Any'}
put_request = requests.put(Update_URL, json = put_body)
put_response= put_request.json()
put_err_desc = put_response.get('error')
if (put_err_desc == 'Unable to update brands') or (put_request.status_code != 200):
    print(put_err_desc)
    print('<br>')
    print("Brand with ID: " +Update_ID+ " does not exist")
    print('<br>')
elif (put_request.status_code == 200):
    print("Brand with ID: " +Update_ID+ " updated")
    print('<br>')
else:
    print(put_err_desc)
    print('<br>')
