import csv,sys,os
from django.db.models import Q
# Path to our django project
project_dir = "/Users/JAI MATA DI/Desktop/Related_Resource/project-lumos-backend/backend"
sys.path.append(project_dir)
os.environ['DJANGO_SETTINGS_MODULE']='settings.development'

import django
django.setup() 	

from courses.models import Language,Domain,SoftSkills,SoftSkillsData,KnowledgeBase,RandomData


def language_import():
	"""
	This function reads the Language.csv file and
	loads it into database
	"""
	# Open the CSV File
	language_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Data-CSV-Files/Language.csv"),
							   delimiter=",")
	# Shift the header from column name to actual value
	language_header = next(language_data)
	# Looping through the entire CSV File and saving it into our model
	for row in language_data:
		language_resource = Language(language_name=row[0],site_url=row[1],description=row[2],icon=row[3])
		language_list=language_resource.save()

	return language_list
language_import()

def domain_import():
	"""
	This function reads the Domain.csv file and
	loads it into database
	"""
	# Open the CSV File
	domain_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Data-CSV-Files/Domain.csv"),
							 delimiter=",")
	# Shift the header from column name to actual value
	domain_header = next(domain_data)
	# Looping through the entire CSV File and saving it into our model
	for row in domain_data:
		domain_resource = Domain(domain_name=row[0],description=row[1],icon=row[2])
		domain_list = domain_resource.save()

	return domain_list
domain_import()

def softskills_import():
	"""
	This function reads the Soft skills.csv file and
	loads it into database
	"""
	# Open the CSV File
	softskills_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Data-CSV-Files/Soft Skills.csv",
		                         encoding="UTF-8"),delimiter=",")
	# Shift the header from column name to actual value
	softskills_header = next(softskills_data)
	# Looping through the entire CSV File and saving it into our model
	for row in softskills_data:
		softskills_resource = SoftSkills(soft_skill_category=row[0],description=row[1],icon=row[2])
		softskills_list = softskills_resource.save()

	return softskills_list
softskills_import()

def softskillsdata_import():
	"""
	This function reads the Soft Skills Data.csv file and
	loads it into database
	"""
	softskillsdata_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Data-CSV-Files/Soft Skills Data.csv",
									 encoding="UTF-8"),delimiter=",")
	softskillsdata_header = next(softskillsdata_data)
	for row in softskillsdata_data:
		softskillsdata_resource = SoftSkillsData(is_active=row[0],title=row[2],description=row[3],
											link_url=row[4],data_type=row[5],paid=row[6])
		softskillsdata_resource.save()
		# For Foreign Key field
		soft_skill = SoftSkills.objects.filter(soft_skill_category=row[1])
		for soft_skills in soft_skill:
			softskillsdata_resource.soft_skill.add(soft_skills)
softskillsdata_import()

def knowledge_base_import():
	"""
	This function reads the Knowledge-Base.csv file and
	loads it into database
	"""
	knowledge_base_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Data-CSV-Files/Knowledge-Base.csv",
									 encoding="UTF-8"),delimiter=",")
	knowledgebase_header = next(knowledge_base_data)
	for row in knowledge_base_data:

		knowledgebase_resource = KnowledgeBase(is_active=row[0],title=row[1],description=row[2],skill_level=row[3],
												data_type=row[4],link_url=row[12],paid=row[13],project=row[14])
		knowledgebase_resource.save()
		# For Foreign Key fields
		languages = Language.objects.filter(Q(language_name = row[5]) | Q(language_name = row[6]) | Q(language_name = row[7]) |
											Q(language_name = row[8]) | Q(language_name = row[9]))
		domains = Domain.objects.filter(Q(domain_name = row[10]) | Q(domain_name = row[11]))
		for language in languages:
			knowledgebase_resource.languages.add(language)
		for domain in domains:
			knowledgebase_resource.domains.add(domain)
knowledge_base_import()

def random_data_import():
	"""
	This function reads the Ramdom Data.csv file and
	loads it into database
	"""
	random_data = csv.reader(open("/Users/JAI MATA DI/Desktop/Data-CSV-Files/Random Data.csv",
							 encoding="UTF-8"),delimiter=",")
	randomdata_header = next(random_data)
	for row in random_data:
		randomdata_resource = RandomData(is_active=row[0],title=row[1],description=row[2],
								link_url=row[3],data_type=row[4],paid=row[5])
		randomdata_list = randomdata_resource.save()

	return randomdata_list
random_data_import()