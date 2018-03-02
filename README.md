# project-lumos-backend

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

3. RowInformation class

  + This class is used to maintain meta information such as is_active (active or not), created_at (when was the object created), modified_at (when was the object last modified). This can  be inherited in other classes to avoid making repeated attributes

4. KnowledgeBase class

  + This class is used to maintain attributes which are common to both the
  Video class and ExternalLink class. It inherits attributes from the RowInformation class. The attributes are title, description, slug, skill_level (to indicate the skill level required by the user to understand the resource), languages (list of languages associated with the resource object), domains (list of domains associated with the resource object)

5. Video class

  + This is a class for resources which are either video or playlists. It inherits from the KnowledgeBase. The attrbutes are video_url along with inherited attributes.

6. ExternalLink class

  + This is a class for resources which are external links, it can be a blog or a tutorial or a course. It inherits from the KnowledgeBase. The attributes are link_url, external_type (to indicate the type of external resource. eg. Blog or Tutorial)

---

It also consists of 4 admin models namely DomainModelAdmin, LanguageModelAdmin, VideoModelAdmin, ExternalLinkModelAdmin

1. LanguageModelAdmin class

  + Handles the admin site for Language class

2. DomainModelAdmin class

  + Handles the admin site for Domain class

3. VideoModelAdmin class

  + Handles the admin site for Video class

4. ExternalLinkModelAdmin class

  + Handles the admin site for ExternalLink class

  The admin models attributes are list_display (attributes to be displayed in the objects list), list_display_links (attributes that will link to detailed view of an object), list_filter (attributes to filter by in the objects list), search_fields (attributes which can be searched on the objects list), autocomplete_fields (get associated attributes from other models), readonly_fields (attributes which are read only in admin site)

 ---

 ### utils

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
