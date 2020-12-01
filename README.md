# para_sa_bata
A project to help Filipino online learners with limited resources to access a question answering chatbot. 

## Required Files for [Geo, the PH Geography Chatbot](https://github.com/albertyumol/para_sa_bata/tree/PH_GeoBot_TeamJulia)
1. [df_consov2.csv](https://github.com/albertyumol/para_sa_bata/blob/PH_GeoBot_TeamJulia/df_consov2.csv) - This contains the complete PH Municipality to PH Province lookup list, which is required for Geo the PH Geography Chatbot to function properly. Place it in the same directory as the jupyter notebook with the complete code.

2. [Customer NER model trained using spaCy](https://drive.google.com/file/d/1xAZ7Juz030esYQUiuAXpw5Z6fLFzUdTw/view) - This 40 MB file contains the custom trained Named Entity Recognition Model for spaCy and it is used to teach the Chatbot about the specific Philippine provinces and municipalities so it can properly identify them as such. Download the file and place the folder in the same directory as the jupyter notebook with the complete code.
