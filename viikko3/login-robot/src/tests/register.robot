*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  seppo  seppo123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  kalle123
    Output Should Contain  Username already taken

Register With Too Short Username And Valid Password
    Input Credentials  aa  aaaaa123
    Output Should Contain  Username too short

Register With Valid Username And Too Short Password
    Input Credentials  seppo  a1
    Output Should Contain  Password too short

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  seppo  seppoabcdefghij
    Output Should Contain  Password must contain also non-alphabets

*** Keywords ***
Input New Command And Create User
    Create User  kalle  kalle123
    Input New Command
