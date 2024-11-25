
class Xpath:
    car_insurance_button = "/html/body/main/div[2]/section/div[4]/a/div[1]/div"
    click_here = '//span[@class ="CarRegDetails_blueTextButton__P1blP blueTextButton fontMedium"]'
    select_city = "//span[text()='Delhi']"
    rto_code = "//li[text()='DL2']"
    brand_type = "//span[text()='MARUTI']"
    model_type = "//li[text()='BALENO']"
    fuel_type = "//li[text()='Petrol'][1]"
    varient_type = '//li[text()="Sigma 1.2 (1197 cc)"]'
    full_name = '//input[@placeholder="Full name"]'
    mobile_no = '//input[@placeholder="Mobile number"]'
    view_price_button = '//button[@class="primaryBtnV2 width-100"]'
    confirm_otp= "//button[text()='Confirm OTP']"
    delivery_details = "//p[text()='In the next 7 days']"
    ex_showroom_price = "//input[@placeholder='Enter ex-showroom price']"
    submit = "//button[text()='Submit']"
    idv_value_change = "//p[@class='fontMedium cursorPointer']"
    idv_value_amount_field = "//input[@type='text']"
    idv_value_update = "//button[@type='button']"
    addon_zero_dep = '(//*[text()="Zero Depreciation"])[1]'
    addon_engine_protector='(//*[text()="Engine Protection Cover"])[1]'
    invoice_price_cover = '(//*[text()="Invoice Price Cover"])[1]'
    tyre_Protector = '(//*[text()="Tyre Protector"])[1]'
    accidental_cover = '(//*[text()="Accident covers"])[1]'
    addon_paid_driver = '(//*[text()="Paid Driver Cover"])[1]'
    accessories_cover = '(//*[text()="Accessories cover"])[1]'
    addon_electrical = '(//*[text()="Electrical Accessories"])[1]'
    addon_electrical_cover_amount = '//*[@placeholder = "Enter amount"]'
    apply_button = '//*[text() = "Apply"]'
    select_insurer = "//img[@alt='ICICI Lombard']//parent::div//following-sibling::div//img[@alt='buy']"
    plan_type = "//p[text()='Plan type']/../following-sibling::div//p"
    idv = "//p[text()='IDV Cover']/../following-sibling::div//p"
    You_will_pay = "//div[@class='totalPay']//div[contains(@class,'redText')]"
    refresh_button = "//*[text()='Refresh the page' and @target='_self']"