# project-lumos-backend


Table of contents
=================

<!--ts-->
   * [Overview](#overview)
   * [Prerequisites](#prerequisites)
   * [Setup](#setup)
   * [Workflow](#workflow)
   * [APPs](#apps)
      * [courses](#courses)
      * [utilities](#utilities)
      * [Ratings](#ratings)
      * [Notes](#notes)
<!--te-->

## Overview

This is the backend repository for Project Lumos, a site that aims to be a central repository for open source knowledge resources. The backend is on Django REST Framework.

## Prerequisites
If you haven't already, install and configure PostgreSQL on your local machine[(guide)](http://www.marinamele.com/taskbuster-django-tutorial/install-and-configure-posgresql-for-django "guide")

create a database table named 'default_db', username being 'username' and password bieng 'password' to use for development.

## Setup
Create a virtual environment in which to install Python pip packages. Use python3

Install development dependencies,

`pip install -r requirements.txt`

---

Create database

`createdb pl_dev`


Setup database tables,

```
python manage.py makemigrations
python manage.py migrate
```

---

Run the web application locally,

`python manage.py runserver --settings=backend.settings.development` # 127.0.0.1:8000(localhost)


you can also set the environment variable in the virtual environment, to avoid writing the settings part everytime

`export DJANGO_SETTINGS_MODULE=backend.settings.development`

## Workflow


### APPs

### courses

This app consists of 6 class models namely Language, Domain, RowInformation, KnowledgeBase, Video and ExternalLink

1. Language class

  + It refers to the various languages in technical skills and soft skills context. This class consists of language attributes    such as language_name(name of the language), slug and languages_for(to indicate technical or soft skills context)

2. Domain class

  + It refers to the various Domains in technical skills and soft skills context. This class consists of domains attributes    such as domain_name(name of the domain), slug and domains_for(to indicate technical or soft skills context)

3. SoftSkills class

  + This class refers to softskills categories. This class consists of softskills attributes such as soft_skill_category, slug, description and icon

4. RowInformation class

  + This class is used to maintain meta information such as is_active (active or not), created_at (when was the object created), modified_at (when was the object last modified). This can  be inherited in other classes to avoid making repeated attributes

5. KnowledgeBase class

  + This class is used to maintain attributes which are common to both the Video class and ExternalLink class. It inherits from RowInformation class. The attributes are title, description, slug, skill_level (to indicate the skill level required by the user to understand the resource), languages (list of languages associated with the resource object), domains (list of domains associated with the resource object), data_type (indicating type of resource, like video or tutorial), paid (indicates whether resource is paid), project (whether resource is a project resource).

6. SoftSkillsData class

  + This class refers to SoftSkills resources. It consists of attributes such as soft_skill, title, description, slug, link_url, data_type and paid

7. RandomData class

  + This class refers to all the random resources. It consists of attributes like title, description, slug, link_url, data_type and paid

---

It also consists of 6 admin models namely DomainModelAdmin, LanguageModelAdmin, SoftSkillsModelAdmin, KnowledgeBaseModelAdmin,
SoftSkillsDataModelAdmin, RandomDataModelAdmin

1. LanguageModelAdmin class

  + Handles the admin site for Language class

2. DomainModelAdmin class

  + Handles the admin site for Domain class

3. SoftSkillsModelAdmin class

  + Handles the admin panel for SoftSkills class

4. KnowledgeBaseModelAdmin class

  + Handles the admin site for KnowledgeBaseModelAdmin class

5. SoftSkillsDataModelAdmin class

  + Handles the admin site for SoftSkillsDataModelAdmin class

6. RandomDataModelAdmin class

  + Handles the admin site for RandomDataModelAdmin class

  The admin models attributes are list_display (attributes to be displayed in the objects list), list_display_links (attributes that will link to detailed view of an object), list_filter (attributes to filter by in the objects list), search_fields (attributes which can be searched on the objects list), autocomplete_fields (get associated attributes from other models), readonly_fields (attributes which are read only in admin site)

#### endpoints
---

1. LanguageViewSet

    handles viewset for LanguageSerializer

    request : https://pl-backend-staging.herokuapp.com/api/language/

    response :

    ```
    {
        "count": 1,
        "next": null,
        "previous": null,
        "results": [
            {
                "url": "https://pl-backend-development.herokuapp.com/api/language/1/",
                "id": 1,
                "language_name": "R",
                "slug": "r",
                "site_url": "https://www.r-project.org/",
                "description": "R is a programming language and software environment for
                statistical computing and graphics supported by the R Foundation for Statistical Computing.",
                "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1b/R_logo.svg/2000px-R_logo.svg.png"
            }
        ]
    }
    ```

     ---

 2. DomainViewSet

      handles viewset for DomainSerializer

      request : https://pl-backend-staging.herokuapp.com/api/domain/

      response :

      ```
      {
          "count": 1,
          "next": null,
          "previous": null,
          "results": [
              {
                  "url": "https://pl-backend-staging.herokuapp.com/api/domain/1/",
                  "id": 1,
                  "domain_name": "Artificial Intelligence",
                  "slug": "artificial-intelligence",
                  "description": "Artificial intelligence (AI, also machine intelligence, MI)
                  is intelligence demonstrated by machines, in contrast to the natural intelligence
                  (NI) displayed by humans and other animals.",
                  "icon": "https://www.iconfinder.com/icons/1106723/ai_artificial_computer_deep_learning_intelligence_machine_learning_icon"
              }
          ]
      }
      ```

       ---

 3. SoftSkillsViewSet

      handles viewset for SoftSkillsSerializer

      request : https://pl-backend-staging.herokuapp.com/api/soft-skills/

      response :

      ```
      {
          "count": 1,
          "next": null,
          "previous": null,
          "results": [
              {
                  "url": "https://pl-backend-staging.herokuapp.com/api/soft-skills/1/",
                  "id": 1,
                  "soft_skill_category": "Body Language",
                  "slug": "body-language",
                  "description": "Does this really matter? Yes it does.SIT UP STRAIGHT!",
                  "icon": ""
              }
          ]
      }
      ```

      ---


 4. SoftSkillsDataViewSet

      handles viewset for SoftSkillsSerializer

      request : https://pl-backend-staging.herokuapp.com/api/soft-skills-data/

      response :

      ```
      {
          "count": 1,
          "next": null,
          "previous": null,
          "results": [
              {
              "url": "https://pl-backend-staging.herokuapp.com/api/soft-skills-data/1/",
              "id": 1,
              "soft_skill": [
                      {
                          "url": "https://pl-backend-staging.herokuapp.com/api/soft-skills/1/",
                          "id": 1,
                          "soft_skill_category": "Time Management",
                          "slug": "time-management",
                          "description": "Time Management",
                          "icon": ""
                      }
              ],
              "title": "How to reduce and cope with stress",
              "description": "It may seem like there’s nothing you can do about stress.",
              "slug": "how-to-reduce-and-cope-with-stress",
              "data_type": "BL",
              "link_url": "https://www.helpguide.org/articles/stress/stress-management.htm",
              "paid": false
              },
          ]
      }    
      ```

      ---

 5. KnowledgeBaseViewSet

      handles viewset for KnowledgeBaseSerializer

      request : https://pl-backend-staging.herokuapp.com/api/knowledge-base/

      response :

      ```
      {
          "count": 1,
          "next": null,
          "previous": null,
          "results": [
              {
                  "url": "https://pl-backend-staging.herokuapp.com/api/knowledge-base/1/",
                  "id": 1,
                  "title": "Testing Django Signals",
                  "description": "Learn how to test Django signals",
                  "slug": "testing-django-signals",
                  "languages": [
                        {
                            "url": "https://pl-backend-staging.herokuapp.com/api/language/1/",
                            "id": 1,
                            "language_name": "Python",
                            "slug": "python",
                            "site_url": "https://www.python.org/",
                            "description": "Python can be easy to pick up whether you're a first-time programmer or you're experienced with other languages.",
                            "icon": "https://upload.wikimedia.org/wikipedia/commons/thumb/0/0a/Python.svg/1200px-Python.svg.png"
                        }
                  ],
                  "domains": [
                        {
                           "url": "https://pl-backend-staging.herokuapp.com/api/domain/1/",
                           "id": 1,
                           "domain_name": "Web Development",
                           "slug": "web-development",
                           "description": "Web development is a broad term for the work involved in developing a web site for the Internet (World Wide Web) or an intranet (a private network).",
                           "icon": "https://cdn3.iconfinder.com/data/icons/web-design-and-development-glyph-vol-1/64/web-development-glyph-01-512.png"
                       }
                  ],
                  "data_type": "BL",
                  "skill_level": "AD",
                  "link_url": "https://medium.freecodecamp.com/how-to-testing-django-signals-like-a-pro-c7ed74279311#.n5anplyc4",
                  "paid": false,
                  "project": false
              },
          ]
      }
      ```

      ---


 6. RandomDataViewSet

      handles viewset for RandomDataSerializer

      request : https://pl-backend-staging.herokuapp.com/api/random-data/

      response :

      ```
      {
          "count": 1,
          "next": null,
          "previous": null,
          "results": [
              {
                  "url": "https://pl-backend-staging.herokuapp.com/api/random-data/1/",
                  "id": 1,
                  "title": "What Are Microservices?",
                  "description": "The article explains in detail what does
                  a microservice architecture mean and what are the use cases where it should be deployed.",
                  "slug": "what-are-microservices",
                  "data_type": "BL",
                  "link_url": "http://microservices.io/patterns/microservices.html",
                  "paid": false
              }
          ]
      }
      ```

      ---

 ---

 ### utilities

 The utils app consists of 2 dependencies

 ---

 1. wikipedia 1.4.0

 To install do

  `pip install wikipedia`

 2. PyDictionary 1.3.4

 To install do

  `pip install PyDictionary`

  ---

  Check out the wikipedia integration here

  [http://127.0.0.1:8000/wiki/test_cases/](http://127.0.0.1:8000/wiki/test_cases/) [Localhost]

  Check out the dictionary integration here

  [http://127.0.0.1:8000/wiki/test_cases/](http://127.0.0.1:8000/wiki/test_cases/) [Localhost]

  Add any slug after /wiki/ or /dict/ to test for yourself

  The wikipedia and dictionary catch the slug (term) from the URL and passes it into the view funtion to return JSON data.

  The view functions are

  ```
  def wikiscript(request, term):
    """
    This is a function that takes in request and a term from url
    which is a slug and runs wikipedia functions to return JSON data
    """
    term = str(term)
    wiki_dict = get_wiki_product_data(term)  #passing the term from url to get_wiki_product_data
    wiki_dict = json.dumps(wiki_dict)  #converting dictionary into JSON
    return JsonResponse(json.loads(wiki_dict))
  ```

  ```
  def dictscript(request, term):
    """
    This is a function that takes in request and a term from url
    which is a slug and runs dictionary function to return JSON data
    """
    term = str(term)
    dict_dict = dictionary_result(term)  #passing the term from url to dictionary_result
    dict_dict = json.dumps(dict_dict)  #converting dictionary into JSON
    return JsonResponse(json.loads(dict_dict))
  ```

 #### endpoints


   7. wikiscript

      This is a function that takes in request and a term from url
      which is a slug and runs wikipedia functions to return JSON data

      request : https://pl-backend-staging.herokuapp.com/wiki/ruby-language/

      response :

      ```
      {
            "wiki_term": "ruby-language",
            "detailed_data": {
            "title": "Ruby (programming language)",
            "url": "https://en.wikipedia.org/wiki/Ruby_(programming_language)",
            "content": "Ruby is a dynamic, reflective, object-oriented,
            general-purpose programming language. It was designed and developed
            "
            },
            "summary_data": {
            "summary_present": true,
            "summary_content": "Ruby is a dynamic, reflective, object-oriented, general-purpose programming language"
            },
            "related_terms": {
            "Ruby (programming language)": "https://en.wikipedia.org/wiki/ruby_(programming_language)",
            "Ruby": "https://en.wikipedia.org/wiki/ruby",
            "Ruby MRI": "https://en.wikipedia.org/wiki/ruby_mri",
            "Ruby on Rails": "https://en.wikipedia.org/wiki/ruby_on_rails",
            "Ruby character": "https://en.wikipedia.org/wiki/ruby_character"
            }
      }
      ```

      ---


   8. dictscript

      This is a function that takes in request and a term from url
      which is a slug and runs dictionary function to return JSON data

      request : https://pl-backend-staging.herokuapp.com/dict/compress/

      response :

      ```
      {
        "term": "compress",
        "term_meaning": {
            "Noun": [
                "a cloth pad or dressing (with or without medication",
                "to relieve discomfort or reduce fever"
            ],
            "Verb": [
                "make more compact by or as if by pressing",
                "squeeze or press together"
            ]
        },
        "term_synonym": [
            "abbreviate",
            "shorten",
            "restrict",
            "wrap",
            "cram"
        ],
        "term_antonym": [
            "amplify",
            "enlarge",
            "increase",
            "lengthen",
            "grow"
        ]
      }
      ```

 ---

 ### Ratings

 ---

 This app consists of 3 class models namely KnowledgeBaseRating, SoftSkillsDataRating, RandomDataRating

1. KnowledgeBaseRating class

  + This class handles the ratings for KnowledgeBase resources

2. SoftSkillsDataRating class

  + This class handles the ratings for SoftSkillsData resources

3. RandomDataRating class

  + This class handles the ratings for RandomData resources

  The ratings classes take a user(if not anonymous user), resource and values for attributes in an object

#### endpoints

1. KnowledgeBaseRatingViewSet

      Handles viewset for KnowledgeBaseRating

      request : https://pl-backend-staging.herokuapp.com/api/knowledge-base-rating/

      response :

      ```
      {
        "count": 1,
        "next": null,
        "previous": "https://pl-backend-staging.herokuapp.com/api/knowledge-base-rating/",
        "results": [
            {
                "url": "https://pl-backend-staging.herokuapp.com/api/knowledge-base-rating/1/",
                "id": 1,
                "user": 1,
                "resource": 9,
                "attribute_1": 2,
                "attribute_2": 3,
                "attribute_3": 4,
                "attribute_4": 3
            }
        ]
    }
      ```

     ---

  2. SoftSkillsDataRatingViewSet

        Handles viewset for SoftSkillsDataRating

        request : https://pl-backend-staging.herokuapp.com/api/softskills-data-rating/

        response :

        ```
        {
          "count": 1,
          "next": null,
          "previous": "https://pl-backend-staging.herokuapp.com/api/knowledge-base-rating/",
          "results": [
              {
                 "url": "https://pl-backend-staging.herokuapp.com/api/knowledge-base-rating/1/",
                 "id": 1,
                 "user": 1,
                 "resource": 9,
                 "attribute_1": 2,
                 "attribute_2": 3,
                 "attribute_3": 4,
                 "attribute_4": 3
             }
           ]
        }
      ```

      ---

  3. RandomDataRatingViewSet

        Handles viewset for RandomDataRating

        request : https://pl-backend-staging.herokuapp.com/api/random-data-rating/

        response :

        ```
        {
          "count": 1,
          "next": null,
          "previous": "https://pl-backend-staging.herokuapp.com/api/random-data-rating/",
          "results": [
              {
                 "url": "https://pl-backend-staging.herokuapp.com/api/random-data-rating/1/",
                 "id": 1,
                 "user": 1,
                 "resource": 9,
                 "attribute_1": 2,
                 "attribute_2": 3,
                 "attribute_3": 4,
                 "attribute_4": 3
             }
           ]
        }
      ```
 ---

 ### Notes

 This app consists of 3 class models namely KnowledgeBaseNotes, SoftSkillsDataNotes, RandomDataNotes

 1. KnowledgeBaseNotes class

  + This model will handle the notes for KnowledgeBase Resource

2. SoftSkillsDataNotes class

  + This model will handle the notes for SoftSkillsData Resource

3. RandomDataNotes class

  + This model will handle the notes for RandomData Resource

  The ratings classes take a user, resource, title, content in an object

#### endpoints

---

1. KnowledgeBaseNotesViewset class

    Handles Views for KnowledgeBaseNotesSerializer

	  request : https://pl-backend-staging.herokuapp.com/api/knowledge-base-notes/

    response :

    ```
         {
            "count": 1,
            "next": null,
            "previous": "https://pl-backend-staging.herokuapp.com/api/knowledge-base-notes/",
            "results": [
              {
                 "url": "https://pl-backend-staging.herokuapp.com/api/knowledge-base-notes/1/",
    			       "id": 1,
    			       "user": 1,
    			       "resource": 9,
    			       "title": "New",
    			       "content": "new",
    			       "slug": "new",
    			       "created_at": "2018-03-15T09:45:10.474941Z",
    			       "modified_at": "2018-03-15T09:46:54.265141Z"
              }
            ]
          }
      ```

   ---

2. SoftSkillsDataNotesViewset class

    Handles Views for SoftSkillsDataNotesViewset

	  request : https://pl-backend-staging.herokuapp.com/api/knowledge-base-notes/

    response :

    ```
         {
            "count": 1,
            "next": null,
            "previous": "https://pl-backend-staging.herokuapp.com/api/soft-skills-data/",
            "results": [
              {
                 "url": "https://pl-backend-staging.herokuapp.com/api/soft-skills-data/1/",
    			       "id": 1,
    			       "user": 1,
    			       "resource": 9,
    			       "title": "New",
    			       "content": "new",
    			       "slug": "new",
    			       "created_at": "2018-03-15T09:45:10.474941Z",
    			       "modified_at": "2018-03-15T09:46:54.265141Z"
              }
            ]
          }
      ```

   ---

3. RandomDataNotesViewset class

    Handles Views for SoftSkillsDataNotesViewset

	  request : https://pl-backend-staging.herokuapp.com/api/random-data-notes/

    response :   

    ```
         {
            "count": 1,
            "next": null,
            "previous": "https://pl-backend-staging.herokuapp.com/api/random-data-notes/",
            "results": [
              {
                 "url": "https://pl-backend-staging.herokuapp.com/api/random-data-notes/1/",
    			       "id": 1,
    			       "user": 1,
    			       "resource": 9,
    			       "title": "New",
    			       "content": "new",
    			       "slug": "new",
    			       "created_at": "2018-03-15T09:45:10.474941Z",
    			       "modified_at": "2018-03-15T09:46:54.265141Z"
              }
            ]
          }
      ```
