from behave import given, when, then
from selenium import webdriver

@given('launch chrome browser')
def launchBrowser(context):
    context.driver.implicitly_wait(10)
    context.driver.maximize_window()
    time.sleep(2)
    context.driver=webdriver.Chrome("C:\Users\HP\PycharmProjects\pythonProject\Drivers\chromedriver.exe")


@when('open the exercise1 values page')
def openHomePage(context):

    context.driver.get("https://www.exercise1.com/values")


@then('Verify the right count of values appears on screen with currency')
def VerifyCount(context):



@then('Verify the value on the screen is greater than \'0\'')
def VerifyValueGreaterThanZero(context, VerifyCount):
    if val_text > 0:
        print(val_text)


@then(u'Verify the total balance is correct based on the value listed on screen')
def VerifyTotalBal(context, VerifyCount):
    total_bal = driver.find_element_by_id("txt_ttl_val")
    if total_bal.is_displayed == True:  # checking for visiblity
        print("The total balance is :" + total_bal.text)


@then(u'Verify the total val matches the sum of values')
def VerifyTotalBalMatch(context):
    val_list = []
    val_list_rows = driver.find_element_by_xpath(
        ".//*[@id='txt_val']/table/tr/td[1]")  # take the toal no of values row 1 to 5
    val_list.append(val_list_rows)
    print("Total number of values row is : " + max(val_list))
    for val in range(max(val_list)):
        total_bal += val_list
    ttl_bal_txt = driver.find_element_by_id("ibl_ttl_val")
    if total_bal == ttl_bal_txt & ttl_bal_txt.is_display == True:
        print("The total balance is : " + ttl_bal_txt)


@then('close the browser')
def CloseBrowser(context):
    context.driver.close()
