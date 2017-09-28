# Resume-Job Matching

Imagine the company you are applying to is a recruiting firm that wants a data scientists to help them build a system for automatically identifying good candidate matches to job openings they are trying to fill.  Let's start with the most basic version of this problem and work our way up. Imagine they have linked-in profiles for candidates with structured data: highest education level, job history (previous titles and employers, with dates), and they even get their eagerness label "actively seeking a new position", "passively looking", "not looking for a new job". They also have a plain text resume for each candidate and a "summary" written by the candidate. For jobs they have listings from Indeed with job title, minimum education levels, company name, company industry.

1. some of the labels for "eagerness" values are missing, design a pipeline to fill in those values 

## Summary

- type: supervised and/or unsupervised, classification and/or regression, indexing, search
- data: semi-structured, unstructured text with some text metadata fields
- data source: scraping or API (Indeed, LinkedIn)
- bigdata: no
- big O: O(N^2)

## Data

A successful dataset might be 

- 10M resumes (text documents) and LinkedIn profiles
  - candidate ID
  - formatted resume/profile text
  - last employer name and job title
  - second-to-last employer name and job title
- 1M job descriptions (from Indeed, Linked-In, etc)
  - job ID
  - job description
  - company description
  - job title
  - company name
  - job descriptions contain unstructured data for education level, salary range, ...
- logfiles for 10,000 interviews/applications and 500 of those were successfully placed
  - activity type: call, email, resume, application, phonescreen, or interview
  - activity date
  - candidate ID
  - job ID

## Model

- What features would you generate
- Feature reduction/selection?
- Feature transformations/combinations?

Describe the pipeline for a PoC (Proof of Concept) or MVP (Minimum Viable Product).
Describe some additional pipeline features

## Evaluation

- What ethical decisions will your algorithm have to make?
- How will you evaluate the ethics of your algorithm?
- How will ethics influence your cross-validation?
