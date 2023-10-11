# Will be converting javascript to python from code below:

'''
import static com.kms.katalon.core.checkpoint.CheckpointFactory.findCheckpoint
import static com.kms.katalon.core.testcase.TestCaseFactory.findTestCase
import static com.kms.katalon.core.testdata.TestDataFactory.findTestData
import static com.kms.katalon.core.testobject.ObjectRepository.findTestObject
import static com.kms.katalon.core.testobject.ObjectRepository.findWindowsObject
import com.kms.katalon.core.checkpoint.Checkpoint as Checkpoint
import com.kms.katalon.core.cucumber.keyword.CucumberBuiltinKeywords as CucumberKW
import com.kms.katalon.core.mobile.keyword.MobileBuiltInKeywords as Mobile
import com.kms.katalon.core.model.FailureHandling as FailureHandling
import com.kms.katalon.core.testcase.TestCase as TestCase
import com.kms.katalon.core.testdata.TestData as TestData
import com.kms.katalon.core.testng.keyword.TestNGBuiltinKeywords as TestNGKW
import com.kms.katalon.core.testobject.TestObject as TestObject
import com.kms.katalon.core.webservice.keyword.WSBuiltInKeywords as WS
import com.kms.katalon.core.webui.keyword.WebUiBuiltInKeywords as WebUI
import com.kms.katalon.core.windows.keyword.WindowsBuiltinKeywords as Windows
import internal.GlobalVariable as GlobalVariable
import org.openqa.selenium.Keys as Keys
import org.openqa.selenium.WebElement as WebElement

WebUI.openBrowser('')

WebUI.navigateToUrl('https://htmlsamplepage.tiiny.site/')

//String tableText = WebUI.getText(findTestObject('Page_Frame Test/td_Cell'))
//println("Table Text: " + tableText)
//String eleText = ''
//WebElement ele1 = WebUI.findWebElement(findTestObject('Page_Frame Test/td_Cell'))
//eleText = ele1.getText()
//println(eleText)
//WebUI.switchToFrame(findTestObject('Page_Frame Test/iframe'), 2)

WebUI.verifyElementPresent(findTestObject('Object Repository/Page_Frame Test/button_Accept All Cookies_onetrust-close-bt_a4e8e4'), 0)

WebUI.click(findTestObject('Object Repository/Page_Frame Test/button_Accept All Cookies'))

WebUI.click(findTestObject('Object Repository/Page_Frame Test/a_Start free trial'))

WebUI.click(findTestObject('Object Repository/Page_Frame Test/button_Accept All Cookies'))

String frameText = WebUI.getText(findTestObject('Page_Frame Test/div_Create a Katalon account'))

println('Frame Text Object: ' + frameText)

WebUI.switchToFrame(findTestObject('Page_Frame Test/iframe'), 2)

String eleText = ''

WebElement ele1 = WebUI.findWebElement(findTestObject('Page_Frame Test/div_Create a Katalon account'))

eleText = ele1.getText()

println('Element Text Object: ' + eleText)

//WebUI.setText(findTestObject('Object Repository/Page_Frame Test/input_Create a Katalon account_user_login'), 'testname')
//WebUI.setText(findTestObject('Object Repository/Page_Frame Test/input_Create a Katalon account_user_email'), 'testemail')
//WebUI.setEncryptedText(findTestObject('Object Repository/Page_Frame Test/input_Create a Katalon account_user_pass'), '5NlMFRvHAa7ATndoAAy6Gg==')
WebUI.closeBrowser()
'''