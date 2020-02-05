# CourseReview-Backend
## Overview
The backend and database for UW-Madison course review website running on Django.

### Course API 
An API containing the following information for all university courses:

{
    "uuid": "",
    "course_name": "",
    "course_number": null,
    "department": [],
    "credits": "",
    "description": "",
    "prereq": "",
    "ethnicStudies": false,
    "genEd": [],
    "breadth": [],
    "level": "",
    "lasCredit": false,
    "typicallyOffered": []
}

### Review API
An API continaining reviews and ratings for university courses

{
    "course": null,
    "review_text": "",
    "difficulty_rating": null,
    "interest_rating": null,
    "success_tips_text": "",
    "date_posted": null,
    "professor": ""
}
