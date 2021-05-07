# DevLink API

### Description

A Django REST API that uses a PostgreSQL database.

### Purpose

The purpose of DevLink is to bridge the gap between qualified developers and companies who have available positions.
Recruiters often deal with many equally qualified candidates on paper but struggle to capture the perfect candidate from
the pool based only on a CV or resume. Our project works to give recruiters and hiring managers multiple qualified
candidates by providing them with candidates who fit their company’s requirements and values. Our questionnaire can be
curated for different lines of industries with an acknowledgment of the technical requirements necessary for a role, but
more importantly, the interpersonal qualifications that make candidates perform successfully and stay with a company.

### Problem

Every developer would like to work in a comfortable environment where they could perform their best. It’s important to
understand what type of team environment a job position will be in. An employer may want a relaxed, upbeat environment
whereas a job-seeker may want an “all-business” environment. Moreover, there isn’t a fully functional application that
helps its recruiters or job seekers in wholly comprehending their degree of match up for a particular position. By
having this feature, our users would save more time in understanding their interests and how well a person fits for a
job. It is at times very difficult for recruiters to truly know an applicant without having an interview with them which
leads to an increment in cost and time for a company. With our application, this problem would be mitigated and would
save lots of time and resources for companies.

### Solution

DevLink connects companies and applicants together through a streamlined process for matching an ideal candidate with an
ideal job. Developers would have the opportunity to select from multiple employers that match their interests and needs
which will lead to increased longevity at the company they ultimately end up working for. Employers would be able to
identify developers whose qualifications both meet that of the company and the role the developers will be applying for
while assessing the applicants who are most aligned to be successful and enjoy the work they do. Employers can gain
insight into their applicant’s personalities and work preferences that extend beyond the capabilities of a CV/resume.
Cover letters will no longer be necessary as candidates can demonstrate their interest in the company by how closely
their aims match those of the job/company they are applying for. A customized questionnaire (the basis for a profile)
allows for employers to select the most qualified candidate for their job from a pool of qualified individuals that may
have similar resumes.

## Instructions

> Warning:  **This application uses environment variables.** Users must contact organization for access.
> Warning:  **This application uses Python 3.9.** :=


Clone the project.
```
git clone https://github.com/countryrudd/api.devlink.tech.git
```

Change directories to within the cloned project.
```
cd api.devlink.tech
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install dependencies required by the DevLink API.
- To install dependencies globally:
    ```
    pip install -d
    ```
- To install dependencies within an environment:
    ```
    pipenv install --python 3.9 -d
    ```

Run database migrations.

```
python manage.py migrate
```

Run the development server at `localhost:8000`.

```
python manage.py runserver
```

## Contributing

Due to this project being a requirement for a Capstone project for ITCS 4155 at the University of North Carolina at
Charlotte, it is closed source. For more information, please refer to the [CONTRIBUTING.md](CONTRIBUTING.md).
