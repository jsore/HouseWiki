# HouseWiki

For the wife and I, an attempt to keep our sanity in check during our house buying process.


<br>


--------------------------------------------------------------------------------------------------
### Wiki structure

What this repo accomplishes. It should be able to do, provide a space for, or track:

<br>

  - [ ] Milestones
    + track list format
    + provide a `textarea` for comments regarding how the milestone was accomplished

<br>

  - [ ] Questions we have that need to be answered
    + unordered list format
    + make them answerable
    + flag them as 'answered' if answered

<br>

  - [ ] Houses section
    + unordered list format, but with a 'ranking' option in the list ( 1 to 3 stars )
    + under each house in the aggregated list of houses and within each house:
      * description of house layout and provide an option to bold any specific description ( for favorites ) and an option of making the text red ( for specific dislikes )
      * section for specific likes and dislikes with optional area for elaborating
      * easily post and navigate through pictures
    + links to floor plans or community websites within each individual house
    + section for questions we may have about each house and community
      * aggregate each question into the 'Questions' section of the wiki
    + grouped by section, organized by highest rank to least
    + sidebar of top 3

<br>

  - [ ] General wish list for what we want in a house and community
    + ordered list
    + items should be able to be ranked favorite to least
    + provide an option to 'flag' the wish as a must or absolute favorite ( bold/red, etc etc )

<br>

  - [ ] General knowledge/home buying tips we want to record

<br>

  - [ ] A secure place for document storage

<br>

  - [ ] Contacts section
    + unordered list format
    + names of people and what they're supposed to help with
    + should actual contact info be listed or not?

<br>

  - [ ] Written in Python + Django because I need live practice with them
    + will there be any problems with this being Python based vs. my site which is Node.js? ( specifically regarding my SSL certs and/or NGINX reverse proxy )








<br><br><br><br>








--------------------------------------------------------------------------------------------------
### Project status updates & roadblocks


  > 'Status' is 'pending' and 'in progress' by default


| Item                   | Type              | Status         | Notes |
|------------------------|-------------------|----------------|-------|
| Get it started         | <ul><li>- [ ] block</li><li>- [x] TODO</li><li>- [ ] other</li></ul> | <ul><li>- [ ] current</li><li>- [x] complete</li><li>- [ ] ignored</li></ul> | README done-ish
|                        |                   |                |       |
| Python env setup (dev) | <ul><li>- [ ] block</li><li>- [x] TODO</li><li>- [ ] other</li></ul> | <ul><li>- [x] current</li><li>- [ ] complete</li><li>- [ ] ignored</li></ul> | virtual env `house-wiki` created/sourced
|                        |                   |                |       |
| Python env setup (prd) | <ul><li>- [x] block</li><li>- [ ] TODO</li><li>- [ ] other</li></ul> | <ul><li>- [ ] current</li><li>- [ ] complete</li><li>- [ ] ignored</li></ul> | conflicts with Node & NGINX proxy?
|                        |                   |                |       |
|                        | <ul><li>- [ ] block</li><li>- [ ] TODO</li><li>- [ ] other</li></ul> | <ul><li>- [ ] current</li><li>- [ ] complete</li><li>- [ ] ignored</li></ul> |
|                        |                   |                |       |
|                        | <ul><li>- [ ] block</li><li>- [ ] TODO</li><li>- [ ] other</li></ul> | <ul><li>- [ ] current</li><li>- [ ] complete</li><li>- [ ] ignored</li></ul> |
|                        |                   |                |       |
|                        | <ul><li>- [ ] block</li><li>- [ ] TODO</li><li>- [ ] other</li></ul> | <ul><li>- [ ] current</li><li>- [ ] complete</li><li>- [ ] ignored</li></ul> |
|                        |                   |                |       |
|                        | <ul><li>- [ ] block</li><li>- [ ] TODO</li><li>- [ ] other</li></ul> | <ul><li>- [ ] current</li><li>- [ ] complete</li><li>- [ ] ignored</li></ul> |


<br><br>


### Supplemental project notes to track for sanity

  > https://github.com/jsore/notes
  >
  > ~~Getting~~ Keeping my thoughts in order


<br><br>


__Python env__

  ```
  …/HouseWiki$ mkdir env

  …/HouseWiki$ virtualenv env/house-wiki

  …/HouseWiki$ source env/house-wiki/bin/activate

  …/HouseWiki$ pip install Django
  …/HouseWiki$ python
  >>> import django
  >>> django.get_version()
  '3.0'
  ```









<br><br><br><br>








--------------------------------------------------------------------------------------------------
### Pending things to add to the Wiki

Just some things I thought to ask or do while thinking up this project.

<details>
<summary>
Click to expand me.
</summary>


<br><br>


__General knowledge, tips__

  - You can apply to other lenders within 15 days without impacting credit


<br><br>


__Things we need to remember to consider__

  - Toll cost
  - Crime rate
  - Traffic
  - School district
  - ( petty ) Sun in eyes during commute or at your back?
  - Cable/internet/electric companies for the area


<br><br>


__Questions for each visited lender/house/community__

  - Builder/lender: Who will oversee the construction?

  - What's your completion date policy? Do we get any sort of SLA if a build is delayed by something not caused by us? Is there an option to hold back funds for builder delays?

  - When can I come see the property during construction? Any rules?

  - What would taxes/insurance/HOA cost for this house?

  - What's the ( more descriptive ) time line of house approval - house built - house move-in ready? What about the community? ( ex: Aubrey @ 8 months vs. Princeton @ 2/3 months )

  - Does the contract have cost escalation clause?

  - What's the timing for 3rd parry new construction for home inspections? ( some builders don't want inspectors on the property during the build process, possibility of poor construction practices )

  - ( during construction ) What's your status on the three inspection milestones? ( before they pour, before drywall, before walk through )

  - Lender: would `any specific agreement signed` have penalties for leaving the home before xx amount of months/years?

  - What's the slope of the lot? ( would it be on a hill, would it be difficult for him to play outside )

  - Do you have a list of vendors we need to meet throughout the process? Where are they located?

  - When are upgrades paid for? Upfront or at closing?



<br><br>



__General Questions__

  - ( For DR Horton ) What are the HBC milestones? What're you looking for when reviewing banking/financial records? Any specificities we need to be aware of for obtaining approval?

  - ( For DR Horton ) Tech specs for smarthome installations? ( Justin is the interested party with this )

  - We've seen Princeton and Aubrey. Are there any other communities near or in between that'd be cheaper?

  - Whats the inspection process like?

  - When we sign a purchase agreement does that lock in the price of the home? ( ex: we give the deposit now to hold a spot while we work on fixing credit and don't sign on a house until xx months later )

  - Can you make additional upgrades once the home started? Any limits on that? ( i.e. nothing structural, etc etc )

  - What is a PID community/neighborhood? Why should we like/dislike it? ( Procure documentation from Cheri, Princeton is PID )

  - What's a MUD community? Why should we like/dislike it?

  - We've seen people with issues with water drainage between lots. Was this resolved? What was the issue? Is there a place where we can file a dispute or claim if we happen to run into this issue, in Aubrey specifically, but also in any other community?

  - What's a Purchase Agreement?

  - What's the difference between a Rate and APR on a mortgage loan?

  - Cheri: is the community USDA?

  - Can you provide us with an HOA rules and regulations sheet?

  - What incentives do you have for using you as a lender? ( get it in writing )


<br><br>


__Wish List__

 - [ ] Good lighting
 - [ ] Good fixtures
 - [ ] __Extra living area__ ( gameroom/bonus room )
 - [ ] __Office space__

<br><br>

__House TODO's__

  - [ ] Look up school ratings in Princeton vs. Aubrey
  - [ ] Organize documents and notes from DR Horton folders
  - [x] Programmatic approach to tracking _<b>all</b> of this_


</details>
