## PATHS ##########################################################################################
env = "LOCAL" #LINODE or LOCAL

if env == "LOCAL":
    directory = "/users/fernando.monaco/desktop/Varie/Briscolaccia/"
else:
    #directory = "home/linux1/briscolaccia/file/"
    directory = "http://148.100.77.173/home/linux1/briscolaccia/file/"
directoryLOG = directory + "LOG/"
directory_ark = directory + "/Archivio/"
# Load your API key from an environment variable or secret management service
logo = directory + "front-End/" + "logo-breno.JPG"
max_tokens = 1000
user = "briscoloni"
password = "suka"

#MODELLI
ada = "text-ada-001"
babbage = "text-babbage-001"
curie = "text-curie-001"
davinci = "text-davinci-003"
chatgpt = "gpt-3.5-turbo"
COMPLETIONS_MODEL = davinci

EMBEDDING_MODEL = "text-embedding-ada-002"
model_embedding = "text-search-babbage-query-001"

cat_list = directory + "biliardoshop-categories.csv"
prd_list = directory + "biliardoshop-prodotti.csv"

label = ["Magio", "Re Perek", "Gazza", "Nando", "Baffo", "Carra", "Aure", "Titti", "Cina", "Dario", "Bruno"]
