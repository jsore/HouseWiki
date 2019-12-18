# HouseWiki

For the wife and I, an attempt to keep our sanity in check during our house buying process.








<br><br><br><br>








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

#### no tags 1, `---` separating each item line

| Item           | Type              | Status         | Notes |
|----------------|-------------------|----------------|-------|
| Get it started | - [ ] roadblock   | - [ ] current  |
|                | - [ ] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |
|----------------|-------------------|----------------|
|                | - [ ] roadblock   | - [ ] current  |
|                | - [x] action item | - [x] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |
|----------------|-------------------|----------------|
|                | - [ ] roadblock   | - [x] current  |
|                | - [ ] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |
|----------------|-------------------|----------------|
|                | - [ ] roadblock   | - [ ] current  |
|                | - [ ] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |

#### no tags 2, no `---` between each item line

| Item           | Type              | Status         | Notes |
|----------------|-------------------|----------------|-------|
| Get it started | - [ ] roadblock   | - [x] current  |
|                | - [x] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |
|                | - [ ] roadblock   | - [ ] current  |
|                | - [ ] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |
|                | - [ ] roadblock   | - [ ] current  |
|                | - [ ] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |
|                | - [ ] roadblock   | - [ ] current  |
|                | - [ ] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |

#### no tags 3, spaces in place of `---` between each item line

| Item           | Type              | Status         | Notes |
|----------------|-------------------|----------------|-------|
| Get it started | - [ ] roadblock   | - [ ] current  |
|                | - [ ] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |
|                |                   |                |
|                | - [x] roadblock   | - [ ] current  |
|                | - [ ] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |
|                |                   |                |
|                | - [ ] roadblock   | - [ ] current  |
|                | - [ ] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |
|                |                   |                |
|                | - [ ] roadblock   | - [x] current  |
|                | - [ ] action item | - [ ] pending  |
|                |                   | - [ ] finished |
|                |                   | - [ ] ignored  |


#### ul/li tags 1, readable structure


| Item           | Type                       | Status                  | Notes |
|----------------|----------------------------|-------------------------|-------|
| Get it started | <ul>                       | <ul>                    |
|                | <li>- [ ] roadblock</li>   | <li>- [ ] current</li>  |
|                | <li>- [ ] action item</li> | <li>- [ ] pending</li>  |
|                | </ul>                      | <li>- [ ] finished</li> |
|                |                            | <li>- [ ] ignored</li>  |
|                |                            | </ul>                   |
|----------------|----------------------------|-------------------------|
|                | <ul>                       | <ul>                    |
|                | <li>- [ ] roadblock</li>   | <li>- [ ] current</li>  |
|                | <li>- [x] action item</li> | <li>- [x] pending</li>  |
|                | </ul>                      | <li>- [ ] finished</li> |
|                |                            | <li>- [ ] ignored</li>  |
|                |                            | </ul>                   |



#### ul/li tags 2, single line for each list

(least favorite)


| Item           | Type              | Status         | Notes |
|----------------|-------------------|----------------|-------|
| Get it started | <ul><li>- [ ] roadblock</li><li>- [x] action item</li></ul> | <ul><li>- [x] current</li><li>- [ ] pending</li><li>- [ ] finished</li><li>- [ ] ignored</li></ul> |
|----------------|-------------------|----------------|
|                | <ul><li>- [ ] roadblock</li><li>- [ ] action item</li></ul> | <ul><li>- [ ] current</li><li>- [x] pending</li><li>- [ ] finished</li><li>- [ ] ignored</li></ul> |
|----------------|-------------------|----------------|
|                | <ul><li>- [ ] roadblock</li><li>- [ ] action item</li></ul> | <ul><li>- [ ] current</li><li>- [ ] pending</li><li>- [ ] finished</li><li>- [ ] ignored</li></ul> |
|----------------|-------------------|----------------|
|                | <ul><li>- [ ] roadblock</li><li>- [ ] action item</li></ul> | <ul><li>- [ ] current</li><li>- [ ] pending</li><li>- [ ] finished</li><li>- [ ] ignored</li></ul> |



1. ( current ) Get it started








<br><br><br><br>








--------------------------------------------------------------------------------------------------
### Pending things to add to the Wiki

Just some things I thought to ask or do while thinking up this project.

<details>
<summary>
Click to expand me.
</summary>


<br><br>


__General knowledge/tips__

  - You can apply to other lenders within 15 days without impacting credit


<br><br>


__Questions for each visited lender/house/community__

  - Builder/lender: Who will oversee the construction?

  - What's your completion date policy? Do we get any sort of SLA if a build is delayed by something not caused by us? Is there an option to hold back funds for builder delays?

  - When can I come see the property during construction? Any rules?

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

<br><br>

__House TODO's__

  - [ ] Look up school ratings in Princeton vs. Aubrey
  - [ ] Organize documents and notes from DR Horton folders
  - [x] Programmatic approach to tracking _<b>all</b> of this_


</details>
