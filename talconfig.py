BASE_DIR = "/opt/boglab"
GENOME_DIR = BASE_DIR + "/genome_data"
GENOME_FILE = GENOME_DIR + "/%s.fasta"
PROMOTEROME_DIR = BASE_DIR + "/promoterome_data"
PROMOTEROME_FILE = PROMOTEROME_DIR + "/%s.fasta"
RVD_SEQ_REGEX = r'^(?:(?:[ACDEFGHIKLMNPQRSTVWY][ACDEFGHIKLMNPQRSTVWY\*])[\s_]+){11,30}(?:[ACDEFGHIKLMNPQRSTVWY][ACDEFGHIKLMNPQRSTVWY\*])$'
#DRUPAL_CALLBACK_URL = "http://talent.local/talent/jobcomplete/"
DRUPAL_CALLBACK_URL = "https://boglab.plp.iastate.edu/talent/jobcomplete/"