## Wine List Data Integration - A Plan

2025-07-17 14:16

To integrate the data into the wine_wiki webapp we need to use migrations and data migrations. The category and subcategory tables need to be established first, then the wine table, followed by population in the same order. The data needs to be prepared on the wine_list_etl end by creating the category, subcategory and wine tables and exporting them as csv for import into the wine_wiki database during the data migration.

TODO:

- [x] prepare category and subcategory tables.
- [x] add category and subcategory tables to etl.
- [x] prepare wine table
- [x] export all
- [x] prepare migration script
- [x] prepare data migration script
- [ ] test
- [ ] run on prod

Also, for reference, the pythonanywhere implementation is prod, the local wine_wiki_site project is dev, there is no test server currently.

## Wine List Data Integration - Migration Scripts

2025-07-21 10:32

The migration script will setup the section, subsection and wine_list tables, followed by a data migration to populate them. What do we need? Start with staging tables that import the data from the csv files then load into a set of related tables. Is that how we do it? Not really. The migration file should only set up the final form of the tables.

So we can 1. create the tables, 2. populate the tables with a `RunSQL` command. According to [this blog](https://simpleisbetterthancomplex.com/tutorial/2017/09/26/how-to-create-django-data-migrations.html) the workflow is to generate a migration file with primary keys/foreign keys as nullable, run that file, then create a data migration file, run that one, then a 3rd file with nullable = False, running that one to establish the relationships.

See how we go.

## Wine List Data Integration - Reassigning Fields

2025-07-22 01:26

Inserting the wine_list_etl data fields into the wine_wiki django database naturally led to some redefinitions of fields - namely the categories to sections, and the disintegration of the wine name field. We now have a number of fields we need to piece together to form the lines. The next task is to assemble 'cuvee_name', 'merged_text_ext', and more to mimic the wine list lines. This may require pushing regex extractions back to the etl pipeline, but im not keen for that atm, that can be a downstream task. The key problem is that merged_text_ext for the most part contains a mish-mash of producer, dryness, cuvee name, volume, region, variety, etc. A ton of fields are null now as well, for example: region, subregion, country, and producer. For the most part section/subsection/subsubsection will populate those fields, but also not..

The most important thing right now is to setup a tabular admin editing interface for the modification of these fields.

## Wine List Data Integration - Giving up on Handson Table

2025-07-22 11:05

Managed to get SOMETHING to load but the docs are very sparse, and frankly it looks like if you want to do anything _fancy_ you should do it in javascript instead, the general consensus is that you use Django for backend, implement a REST API then React for the frontend. Which I'm ok with, but not right now. Now I want to push out a functional product. So. The best method of organising the data as it stands is to identify which fields need to be populated in the wine list and get to modification via a spreadsheet program. To do this we need to identify what fields go where and what content needs to be in them.

The wine list is laid out as follows:

vintage, Producer, Cuvee (optional) Region, State/Country, Volume (Optional) Price.

## Wine List Data Integration - Developing a Spreadsheet Tool

2025-07-22 14:03

I have worked through about 1/3 of the wines (champagne and german/austrian riesling being the most complicated) and have realised that to do this properly we need to add some indicator columns, namely a column to show what text has been extracted and an indicator whether the wine is determined to be adequately extracted. The first can be done by substituting the string that is to be extracted with the extracted text, then testing whether the string is empty or not. To do this we need to also have a column for correcting the input text to be extracted as the pdf extraction pipeline mangled a fair quantity of the text. Finally, we need to extract the strings exactly as they appear, for example 'fr' must be extracted as 'fr', not 'france', and we can add more meaning to it later.

The alternative is a lot of case statements..

## Wine List Data Integration - Progress Report

2025-07-25 14:13

So I've managed to extract all the data out of the wine list text into a big wine_list table. Now to get it into the website, again.

## Wine List Data Integration - Initial Steps Completed

2025-07-25 15:52

Ok, its done. A pipeline exists to get all the information from the wine list and it is displaying correctly. Now there is a ton of things to fix:

- [x] reconcile settings between the prod and dev server
- [x] Fix "None" fields in list and wine page
- [x] correct display order of sections
- [ ] add subsubsection headers
- [ ] fix update wine success
- [ ] figure out method of updating from current uploaded list file.
- [ ] figure out method of backing up data
- [ ] add producer page
- [ ] add geographical unit page
- [ ] add classification page
- [ ] add user accounts
- [ ] add login requirement for all pages
- [ ] add "active" or "inactive" field for wines.
- [ ] add copy of current wine list to website.

## Wine List Development - Reconciling Settings between Prod and Dev Server

2025-07-25 17:09

[Stackoverflow](https://stackoverflow.com/questions/10664244/django-how-to-manage-development-and-production-settings) recommends using the DJANGO_SETTINGS_MODULE env var. So we can store both settings in the repo and set it in the env var. It simply uses the python module import syntax. As you can import into the settings file at runtime, common settings can live in a `common_settings` module which is imported into `prod_settings`, `dev_settings` etc. and its values overridden within the respective settings module. In [pythonanywhere](https://help.pythonanywhere.com/pages/EnvironmentVariables) the advice is to use python dotenv then call `load_dotenv` in the pythonanywhere WSGI file.

So we're going to want to save the local settings file as the common_settings file, the file on the server as `prod_settings`, create an empty `dev_settings`, import into dev_settings and prod_settings, create the file.. ugh.

## Wine List Development - Progress Report

2025-07-26 01:40

Looking good. Sorted out the settings, fixed the None fields and ordering. Just need to keep moving through the list. Subsubsection headers will be annoying but shouldnt be too difficult.

## Wine List Development - Adding SubSubSection

2025-07-27 10:22

Subsubsection header adds a 3rd level of nesting to the grouped dict in WineListView.

We dont actually need to seperate subsubsection table, but we should for consistency. Doesnt actually need seperation, just redefinition as the column as foreign key and creation of the table.

TODO:

- [x] create a subsubsection table with an ordering.
- [x] redefine subsubsection as a foreign key to the table with the ordering.
- [x] add ordering by subsubsection in WineListView
- [x] add `wine.subsubsection` level nesting.
- [ ] add a 3rd level of nesting to the conversion from dict to grouped_dict on line 58.

## Wine List Development - Reevaluation of Strategy

2025-07-31 00:10:25

So. I didn't expect the guys to start using the app so quickly, and now I need to manage their data additions while developing what is really an alpha++ system. While trying to add subsubsections I had modified the initial migration to include subsubsection as a foreign key and restructured the migrations to act as though it always was, which is fine as long as I was willing to completely rebuild the database along the way, but now I'm not because I have no idea what the guys have added or not. Ha. And if I wipe their data they'll quickly lose interest. So its really important to add data integrity over feature addition. They don't seem phased by the subsubsection problem, so data integrity is most important. The best way to start working on this is to go back to the prod branch level in dev and start working on that problem, and avoid any further modifications of the migration legacy. Problem with that is that some good changes have been added but not possibly pulled into prod yet. Will have to look into that. Also we should discard any changes to the migrations and then start looking at data integrity first. To do this:

- [x] look at where prod is at relative to dev
- [x] swap dev to prod
- [x] branch dev as dev
- [ ] fix wine update success url
- [ ] add backup solution
- [ ] add date modified recording to wine update
- [ ] add modifier initials field
- [ ] add user accounts
- [ ] add automatic connection of user to update
- [ ] improve wine update UX by grouping fields
- [ ] add formal revision recording
- [ ] lazy loading of wine list, or pagination.

To look where prod is relative to dev, I'll need to log into the prod server and check the current commit hash, and look at what I've added since. What is that? 877fd804bb79ca0f3505dfc44cc2be3bcdd31776 - Saturday 01:42. (doesnt look like pythonanywhere is using my local time. Fix that?)

So 3 commits, and only the last 1 changes the migrations (I think, need to confirm). Need to now double check the commits to ensure they dont touch migration, push those to prod while performing the opposite with the latest commit and any current uncommited changes - adding changes that dont affect migration. Can I ammend the commit messages to be more clear?

The simplest method should be to create a dev branch then reset main to be the same as prod. Then start bisecting the dev branch, moving migration related changes to a mod-migration branch, testing other changes and pushing them to prod to continue to deliver QoL updates.

Summary:

- [x] create dev branch
- [x] reset prod (main) to same as prod env.
- [x] bisect dev branch to seperate non-migation changes from migration changes
- [x] test non-migration branch and push successful changes to prod

What are the changes to be bisected? What is the strategy?

## Wine List Development - Lost Some Logs

2025-08-02 15:04

Lost some logs when checking out main from dev. didnt know that could happen. Anyway, setup of the dev/main branches is complete and the migration commits separated out. Now need to move the commits into main from dev and test. The question is what is the best way to do that, rebase or merge?

Rebase is used to make main look like its built on top of dev, rewriting the history. dont want that. merge or cherry-pick. Cherry-pick for subsets, merge for everything. We can test it by branching main, cherrypicking then rebasing.

## Wine List Development - Dev Prod Flow Successful

2025-08-02 17:33

Have successfully moved to a dev prod branch flow, as described previously. Work and test on dev, merge into main then push and pull. This flow enables and enforces incremental modifications followed by testing to ensure that changes work as intended and causes of error can be tracked.

Now to fix the success url and add markdown support.
