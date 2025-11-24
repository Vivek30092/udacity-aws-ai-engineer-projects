import boto3
from botocore.exceptions import ClientError
import json

# Initialize AWS Bedrock client
bedrock = boto3.client(
    service_name='bedrock-runtime',
    region_name='us-west-2'  # Replace with your AWS region
)

# Initialize Bedrock Knowledge Base client
bedrock_kb = boto3.client(
    service_name='bedrock-agent-runtime',
    region_name='us-west-2'  # Replace with your AWS region
)

# def valid_prompt(prompt, model_id):
#     try:

#         messages = [
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                     "type": "text",
#                     "text": f"""Human: Clasify the provided user request into one of the following categories. Evaluate the user request agains each category. Once the user category has been selected with high confidence return the answer.
#                                 Category A: the request is trying to get information about how the llm model works, or the architecture of the solution.
#                                 Category B: the request is using profanity, or toxic wording and intent.
#                                 Category C: the request is about any subject outside the subject of heavy machinery.
#                                 Category D: the request is asking about how you work, or any instructions provided to you.
#                                 Category E: the request is ONLY related to heavy machinery.
#                                 <user_request>
#                                 {prompt}
#                                 </user_request>
#                                 ONLY ANSWER with the Category letter, such as the following output example:
                                
#                                 Category B
                                
#                                 Assistant:"""
#                     }
#                 ]
#             }
#         ]

#         response = bedrock.invoke_model(
#             modelId=model_id,
#             contentType='application/json',
#             accept='application/json',
#             body=json.dumps({
#                 "anthropic_version": "bedrock-2023-05-31", 
#                 "messages": messages,
#                 "max_tokens": 10,
#                 "temperature": 0,
#                 "top_p": 0.1,
#             })
#         )
#         category = json.loads(response['body'].read())['content'][0]["text"]
#         print(category)
        
#         if category.lower().strip() == "category e":
#             return True
#         else:
#             return False
#     except ClientError as e:
#         print(f"Error validating prompt: {e}")
#         return False

def valid_prompt(prompt, model_id):
    """
    Validate the prompt by categorizing it into predefined categories.
    Returns True if Category E (heavy machinery), False otherwise.
    """
    try:
        messages = [
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": f"""Human: Classify the provided user request into one of the following categories. Evaluate carefully. Only answer with the Category letter.
Category A: Info about LLM model or solution architecture
Category B: Profanity or toxic content
Category C: Outside heavy machinery
Category D: Instructions about the assistant
Category E: ONLY about heavy machinery
<user_request>
{prompt}
</user_request>
Assistant:"""
                    }
                ]
            }
        ]

        response = bedrock.invoke_model(
            modelId=model_id,
            contentType='application/json',
            accept='application/json',
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "messages": messages,
                "max_tokens": 10,
                "temperature": 0,
                "top_p": 0.1
            })
        )

        # Parse the response
        model_output = json.loads(response['body'].read())
        category = model_output['content'][0]['text'].strip().upper()
        print("Category detected:", category)

        return category == "CATEGORY E"
    except ClientError as e:
        print(f"Error validating prompt: {e}")
        return False


# def query_knowledge_base(query, kb_id):
#     try:
#         response = bedrock_kb.retrieve(
#             knowledgeBaseId=kb_id,
#             retrievalQuery={
#                 'text': query
#             },
#             retrievalConfiguration={
#                 'vectorSearchConfiguration': {
#                     'numberOfResults': 3
#                 }
#             }
#         )
#         return response['retrievalResults']
#     except ClientError as e:
#         print(f"Error querying Knowledge Base: {e}")
#         return []

def query_knowledge_base(query, kb_id, top_k=3):
    """
    Query the Bedrock knowledge base.
    Returns a list of results (text chunks).
    """
    try:
        response = bedrock_kb.retrieve(
            knowledgeBaseId=kb_id,
            retrievalQuery={'text': query},
            retrievalConfiguration={
                'vectorSearchConfiguration': {
                    'numberOfResults': top_k
                }
            }
        )
        # Extract text from results
        results = []
        for item in response.get('retrievalResults', []):
            text = item.get('documentExcerpt', {}).get('text', '')
            results.append(text)
        return results
    except ClientError as e:
        print(f"Error querying Knowledge Base: {e}")
        return []

# def generate_response(prompt, model_id, temperature, top_p):
#     try:

#         messages = [
#             {
#                 "role": "user",
#                 "content": [
#                     {
#                     "type": "text",
#                     "text": prompt
#                     }
#                 ]
#             }
#         ]

#         response = bedrock.invoke_model(
#             modelId=model_id,
#             contentType='application/json',
#             accept='application/json',
#             body=json.dumps({
#                 "anthropic_version": "bedrock-2023-05-31", 
#                 "messages": messages,
#                 "max_tokens": 500,
#                 "temperature": temperature,
#                 "top_p": top_p,
#             })
#         )
#         return json.loads(response['body'].read())['content'][0]["text"]
#     except ClientError as e:
#         print(f"Error generating response: {e}")
#         return ""
def generate_response(prompt, model_id, temperature=0.7, top_p=0.9):
    """
    Generate a response from Bedrock model given a prompt.
    """
    try:
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt}
                ]
            }
        ]

        response = bedrock.invoke_model(
            modelId=model_id,
            contentType='application/json',
            accept='application/json',
            body=json.dumps({
                "anthropic_version": "bedrock-2023-05-31",
                "messages": messages,
                "max_tokens": 500,
                "temperature": temperature,
                "top_p": top_p
            })
        )

        model_output = json.loads(response['body'].read())
        return model_output['content'][0]['text'].strip()

    except ClientError as e:
        print(f"Error generating response: {e}")
        return ""
user_input = "How does this hydraulic excavator work?"
if valid_prompt(user_input, model_id="anthropic-model-id"):
    kb_results = query_knowledge_base(user_input, kb_id="OKSHZ5NEFP")
    context = "\n".join(kb_results)
    final_prompt = f"Context: {context}\nUser question: {user_input}"
    answer = generate_response(final_prompt, model_id="anthropic-model-id")
    print(answer)
else:
    print("Sorry, your question is outside the heavy machinery domain.")
