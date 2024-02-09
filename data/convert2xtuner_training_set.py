import ujson

converted_data = []
source_dir = fr'/root/ft-cc/data/smile/data'

def convert2set(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        conversation = ujson.load(file)
        converted_conversation = []
        for item in conversation:
            if item["role"] == "client":
                converted_conversation.append({"input": item["content"], "output": ""})
            elif item["role"] == "counselor":
                converted_conversation[-1]["output"] = item["content"]
        converted_data.append({"conversation": converted_conversation})



def convert_all_sessions():

    for idx in range(56032):
        try:
            convert2set(f'{source_dir}/{idx}.json')
        except Exception as e:
            pass
    # Step 3: Add system responses to each conversation
    for conv in converted_data:
        for exchange in conv["conversation"]:
            exchange["system"] = "A professional psychological counselor with extensive knowledge in psychology and mental health. You are skilled in using various psychological counseling techniques, such as principles of cognitive-behavioral therapy, motivational interviewing techniques, and problem-solving oriented short-term therapies. Show empathy and profound understanding of the visitor's feelings in a warm and friendly tone. Communicate with visitors in a natural way, avoiding overly long or short responses, and ensuring smooth and human like responses. Provide in-depth guidance and insights, using specific psychological concepts and examples to help visitors explore their thoughts and feelings more deeply. Avoid instructional responses and prioritize empathy and respect for the visitor's feelings. Adjust the response based on the visitor's feedback to ensure that it fits the visitor's context and needs."

    # Step 5: Save the merged conversations to a new JSON file
    output_file = "conversations.json"
    with open(output_file, "w", encoding="utf-8") as file:
        ujson.dump(converted_data, file, indent=4, ensure_ascii=False)

    print(f"Conversion completed and saved to {output_file}.")


if __name__ == '__main__':
    convert_all_sessions()