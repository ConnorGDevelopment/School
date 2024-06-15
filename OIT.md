# OIT Training

## Copy/Pastes

### Waiting for Customer

```
This ticket is being resolved due to inactivity. If you should need to re-open this ticket, you will need to respond here within 7 days or it will automatically close. If you are needing further assistance after those 7 days you will need to put in a new service or incident request.
Thanks,
IT Service Desk
E: <servicedesk@ohio.edu>
P: 740-593-1222 
W: https://help.ohio.edu/TDClient/30/Portal/Home/
```

### Ohio ID Request

```
After the customer gave us their PID we gave them their Ohio ID.
```

### PID Request

```
After confirming the customer's ID we gave them their PID.
```

### Instruct to Password Reset

```
The customer called asking to reset their password so we directed them to account.ohio.edu where they could reset it.
```

### Add Number to Azure Account

```
The customer changed phones, after confirming their identity we added the new number and had them go to myaccount.microsoft.com to add the authenticator app along with any other methods they would like.
```

### Reset Azure Account

```
The customer changed phones, after confirming their identity we reset their azure account so that it will prompt them to set it up again.
```

### Unlock Azure Account

```
The customer's account was locked, after confirming their identity we removed the lock and advised them to wait 20 min before logging in to set up Azure.
```

### Instruct to Reset OhioID

```
After confirming the customer’s account, we reset it and advised them to go to account.ohio.edu to reactivate the account.
```

## Links

### Jabber (Program)

### Cisco Finesse

https://uccxpri.oit.ohio.edu:8445/desktop/logon.html?locale=en_US&error=true&isSSO=false

*Requires Jabber to be Logged In*

Ext. 5555930511

### Ivy (Chatbot)

https://app.ivy.ai/admin/analytics/dashboards/bot

### IDM

https://idm.ohio.edu/itim/console/main

### Ticket Dashboard (TDX)

https://help.ohio.edu/TDNext/Home/Desktop/Default.aspx

### Last 5 Minutes

1. Turn Off Phone in Cisco Finesse
2. Enter Hours
3. Clear out Waiting for Customer

## Confirm ID

Confirm the following:

1. DOB
2. Last 4 SSN
3. Full Name

## Choose Ticket Form

### General

(Passwords & Password Reset) MyID
: Error when changing password
: Needing password reset

(Service Desk) Information Request
: Random calls asking nonsense
: Requestor/Contact Required -> unknown@ohio.edu

(Service Desk) Call Transfer
: Can use unknown@ohio.edu as recipient
: Include where you transferred them to in description

#### Fields

Set Source: Phone || Email || Chat Bot

Set Status: Resolved || New

Detail
: Not all tickets have this field, usually you set to General

Priority
: Can adjust based on customer description

Urgency
: Do not change unless the issue is "OU Police phones are down" -> Then set to Emergency

Assignees & Notifications / Escalation Path
: We are first step, if we have to escalate ticket then find them by the Dept listed.

### ETextbook

(Digital Course Materials) Inclusive Access
: Inclusive Access Charge

### Username from PID

(Service Desk) Information Request
: Generally confused people call, they don't know their OU email or username or they are trying to log into OU using outlook
: Can give username with PID
: Search by Full Name if they have neither username or PID, formatted as First*Last and search bar set to Full Name
: Last 2 digits of OU ID are year created

If no recovery information or incorrect recovery information, have to reset account instead of password.

### Instruct to Reset Password

account.ohio.edu/myid/ -> Existing User -> Reset Password -> Enter Code

Don't read out their recovery email, they will see it when they get to enter code

### PID from Username [Requires ID]

Confirm ID when giving out PID

DOB, FullName, Last4SSN

### Reset Account [Requires ID]

After ID confirm -> Set Activated to Inactivated -> Submit

(Passwords & Password Reset) MyID
: Form when you instruct someone how to reset password

Takes 1 hour to process

### Reset Authenticator [Requires ID]

If they change phones

### Blackboard

*Remember to ask for Course ID*

*When transferring to Blackboard Support, always do 'warm' transfer (talk to recipient).*

Incident / (Learning Management System) Blackboard
: Something is broken with Blackboard

Service Request / (Learning Management System) Blackboard
: Everything else happening related to Blackboard

Detail
: Add/Modify Users -> TA needs to be added into course
: Merge Course Sections -> Will be explicitly asked for by Prof
: General -> Everything Else
: Archiving -> Request for course that has been closed
: Course Organization Request & Integration Support -> Never used

Can transfer people there, don't give number out.

### Canvas

*When transferring to Canvas, always do 'cold' transfer.*

## Waiting for Customer Ticket

1. Actions
2. Update
3. Change Status from Waiting for Customer to Resolved

## Etiquette

1. Always help to the best of your ability
   1. If someone calls and says "I meant to call someone else", ask who and see if you can direct them
2. When referring to someone, refer to them as the customer
3. When someone asks when ticket will be resolved say 24-48 hours
   1. Can also mention you don't know how many of the same ticket are open, so can't estimate

## Other

We are also referred to as Contact Center

Acct/Dept
: Generally required when present, sort by id -> Ohio University (id 3)

### Clear Cache (Chrome): ctrl + shift + del

### [Knowledge Base](https://help.ohio.edu/TDClient/30/Portal/KB/)

### Add Non-Computer/Mobile Device to WiFi (Game Console, TV, etc)

Have to register and connect to Guest, cannot connect to eduroam
wireless.ohio.edu

Can take up to 24 hours

### 'Fixing Account' [Requires ID]

Confirm ID -> Set to Activated
If no roles then search role / role is 3 - Terminated -> add role 'restore'

## Taking a Break

Cisco -> Set to Break Time
Teams -> Post in Service Desk Status
