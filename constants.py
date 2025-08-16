## PATHS ##########################################################################################
env = "LOCAL" #LINODE or LOCAL

if env == "LOCAL":
    directory = "/users/fernando.monaco/desktop/Varie/Briscolaccia/"
else:
    directory = "/root/AI/Briscolaccia/"

directoryLOG = directory + "LOG/"
directory_ark = directory + "/Archivio/"
# Load your API key from an environment variable or secret management service
mia_key = ""
acn_key = "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"
anthropic_api_key = "sk-7VDDmz1_M8BsqyhN8YC80dF9Kpt18DxFett7LW3EDLlcJda2Fx3B3ORC2QGGBx_iK5USWHxXbvoQDsF7m9l5UA"

max_tokens = 1000

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

label = ["Magio", "Re Perek", "Gazza", "Nando", "Baffo", "Carra", "Aure", "Titti", "Cina", "Dario"]