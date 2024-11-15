# GitHub Users in Bangalore

This repository contains data about GitHub users in Bangalore with over 100 followers and their repositories.

## Files

1. `users.csv`: Contains information about 602 GitHub users in Bangalore with over 100 followers
2. `repositories.csv`: Contains information about 50242 public repositories from these users
3. `gitscrap.py`: Python script used to collect this data

## Data Collection

- Data collected using GitHub API
- Date of collection: 2024-10-31
- Only included users with 100+ followers
- Up to 500 most recently pushed repositories per user

  ## Most interesting Fact
- GOOGLE has only 15 employees in Bangalore that are highly active on GitHub.
- Even though JavaScript is used on frontend it still has a high number of users.
- Make sure you learn Javascript and HTML as it has very high demand and also is used a lot.

  ## Actionable Recommendation For Developers
- Be highly Active on Github as MORE REPOS = HIGH FOLLOWERS = BETTER RESULT = HIGH SALARY JOB

  ## ABOUT users.csv
- users.csv has following information about each user in Bangalore with over 100 followers, with fields:

login: Their Github user ID
name: Their full name
company: The company they work at. Clean up company names. At least make sure:
They're trimmed of whitespace
Leading @ symbol is stripped (Note: ONLY the first one is stripped)
They are converted to UPPERCASE
location: The city they are in
email: Their email address
hireable: Whether they are open to being hired
bio: A short bio about them
public_repos: The number of public repositories they have
followers: The number of followers they have
following: The number of people they are following
created_at: When they joined Github


  ## ABOUT repositories.csv
- repositories.csv has these users' public repositories. For each user in users.csv, fetch up to the 500 most recently pushed repositories, with fields:

login: The Github user ID (login) of the owner, which, BTW, is not directly in the API response.)
full_name: Full name of the repository
created_at: When the repository was created
stargazers_count: Number of stars the repository has
watchers_count: Number of watchers the repository has
language: The programming language the repository is written in
has_projects: Whether the repository has projects enabled
has_wiki: Whether the repository has a wiki
license_name: Name of the license the repository is under (This is under license.key)

## The Purpose of this porject was to solve these questions which can be answered through the .py files attached in the repositories.
1. Who are the top 5 users in Bangalore with the highest number of followers? List their login in order, comma-separated.
Users
2. Who are the 5 earliest registered GitHub users in Bangalore? List their login in ascending order of created_at, comma-separated.
Users
3. What are the 3 most popular license among these users? Ignore missing licenses. List the license_name in order, comma-separated.
Licenses
4. Which company do the majority of these developers work at?
Company (cleaned up as explained above)
5. Which programming language is most popular among these users?
Language
6. Which programming language is the second most popular among users who joined after 2020?
Language
7. Which language has the highest average number of stars per repository?
Language
8. Let's define leader_strength as followers / (1 + following). Who are the top 5 in terms of leader_strength? List their login in order, comma-separated.
User login
9. What is the correlation between the number of followers and the number of public repositories among users in Bangalore?
Correlation between followers and repos (to 3 decimal places, e.g. 0.123 or -0.123)
10. Does creating more repos help users get more followers? Using regression, estimate how many additional followers a user gets per additional public repository.
Regression slope of followers on repos (to 3 decimal places, e.g. 0.123 or -0.123)
11. Do people typically enable projects and wikis together? What is the correlation between a repo having projects enabled and having wiki enabled?
Correlation between projects and wiki enabled (to 3 decimal places, e.g. 0.123 or -0.123)
12. Do hireable users follow more people than those who are not hireable?
Average of following per user for hireable=true minus the average following for the rest (to 3 decimal places, e.g. 12.345 or -12.345)
13. Some developers write long bios. Does that help them get more followers? What's the impact of the length of their bio (in Unicode words, split by whitespace) with followers? (Ignore people without bios)
Regression slope of followers on bio word count (to 3 decimal places, e.g. 12.345 or -12.345)
14. Who created the most repositories on weekends (UTC)? List the top 5 users' login in order, comma-separated
Users login
15. Do people who are hireable share their email addresses more often?
[fraction of users with email when hireable=true] minus [fraction of users with email for the rest] (to 3 decimal places, e.g. 0.123 or -0.123)
16. Let's assume that the last word in a user's name is their surname (ignore missing names, trim and split by whitespace.) What's the most common surname? (If there's a tie, list them all, comma-separated, alphabetically)
Most common surname(s)

Every question can be answered by running the .py files with the corresponding question number.

- Happy Learning 😊 (Aary Ninja)

