*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page And Check Is Open

*** Test Cases ***
Register With Valid Username And Password
    Set Username  seppo
    Set Password  seppo123
    Confirm Password  seppo123
    Submit Registration
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  se
    Set Password  seppo123
    Confirm Password  seppo123
    Submit Registration
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  seppo
    Set Password  se
    Confirm Password  se
    Submit Registration
    Register Should Fail With Message  Password too short

Register With Nonmatching Password And Password Confirmation
    Set Username  seppo
    Set Password  seppo123
    Confirm Password  seppo456
    Submit Registration
    Register Should Fail With Message  Password does not match password confirmation

Login After Successful Registration
    Set Username  teppo
    Set Password  teppo123
    Confirm Password  teppo123
    Submit Registration
    Go To Login Page
    Set Username  teppo
    Set Password  teppo123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Set Username  keppo
    Set Password  keppo123
    Confirm Password  teppo123
    Submit Registration
    Go To Login Page
    Set Username  keppo
    Set Password  keppo123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Page Should Contain  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Submit Registration
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Confirm Password
    [Arguments]  ${confirmation}
    Input Password  password_confirmation  ${confirmation}

Go To Register Page And Check Is Open
    Go To Register Page
    Register Page Should Be Open
