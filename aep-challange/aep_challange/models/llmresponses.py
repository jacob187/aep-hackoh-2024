import pandas as pd
from langchain import LLMChain

df=pd.read_csv(             )
first_column_values=df.iloc[:,0].tolist()

llm= WHATEVER MODEL YOU USE

def categorize_sentence(value):
  prompt=("You are a categorization assistant. Categorize the following sentence into one of the categories: "
        "Positive, Negative, Neutral, Informative.\n\n"
        f"Sentence: '{value}'")
  chain = LLMChain(llm=llm, prompt=prompt)
  return chain.run()

results = []
for value in first_column_values:
    categorized = categorize_sentence(value)
    results.append((value, categorized))

results_df = pd.DataFrame(results, columns=['Original', 'Category'])
results_df.to_csv('categorized_sentences.csv', index=False)

