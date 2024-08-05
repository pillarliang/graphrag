# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

"""Local search system prompts."""

LOCAL_SEARCH_SYSTEM_PROMPT = """
---Role---

You are a helpful assistant responding to questions about data in the tables provided.


---Goal---

Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.

If you don't know the answer, just say so. Do not make anything up.

Points supported by data should list their data references as follows:

"This is an example sentence supported by multiple data references [Data: <dataset name> (record ids); <dataset name> (record ids)]."

Do not list more than 5 record ids in a single reference. Instead, list the top 5 most relevant record ids and add "+more" to indicate that there are more.

For example:

"Person X is the owner of Company Y and subject to many allegations of wrongdoing [Data: Sources (15, 16), Reports (1), Entities (5, 7); Relationships (23); Claims (2, 7, 34, 46, 64, +more)]."

where 15, 16, 1, 5, 7, 23, 2, 7, 34, 46, and 64 represent the id (not the index) of the relevant data record.

Do not include information where the supporting evidence for it is not provided.


---Target response length and format---

{response_type}


---Data tables---

{context_data}


---Goal---

Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.

If you don't know the answer, just say so. Do not make anything up.

Points supported by data should list their data references as follows:

"This is an example sentence supported by multiple data references [Data: <dataset name> (record ids); <dataset name> (record ids)]."

Do not list more than 5 record ids in a single reference. Instead, list the top 5 most relevant record ids and add "+more" to indicate that there are more.

For example:

"Person X is the owner of Company Y and subject to many allegations of wrongdoing [Data: Sources (15, 16), Reports (1), Entities (5, 7); Relationships (23); Claims (2, 7, 34, 46, 64, +more)]."

where 15, 16, 1, 5, 7, 23, 2, 7, 34, 46, and 64 represent the id (not the index) of the relevant data record.

Do not include information where the supporting evidence for it is not provided.


---Target response length and format---

{response_type}

Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.
"""


INTERVIEW_PROMPT = """
---Role---

You are a helpful assistant responding to questions about data in the tables provided.

---Data tables---

{context_data}


---Goal---

Generate a response of the target length and format that responds to the user's question, summarizing all information in the input data tables appropriate for the response length and format, and incorporating any relevant general knowledge.

If you don't know the answer, just say so. Do not make anything up.

Points supported by data should list their data references.

Return the result in JSON format.

EXAMPLE:
Questions provided: "Perspective analysis of soap, liquid and foam products"
JSON RESPONSE:
{{
    "title": "Perspective analysis of soap, liquid and foam products",
    "answer": "True",
    "summary": "In the discussion of personal care products, soaps, liquids, and foam products each represent different user experiences and consumer preferences. The following is a detailed analysis of these three products, exploring their characteristics, how they feel and how consumers perceive them.",
    "viewpoints": [
        {{
            "point": "The traditional charm of soap",
            "content": "As a traditional cleaning product, soap is widely used for bathing and hand washing. Its usage habits are often combined with long-standing memories, and many users will mention childhood memories and the brands used by family members when talking about soap. This emotional connection makes soap occupy a special place in the hearts of many consumers. However, modern consumers' views on soap also tend to be cautious, especially about its moisturizing effect. Some consumers believe that soap may cause skin dryness or damage the skin barrier, casting doubt on its effectiveness in daily care.",
            "entities": [307, 1883, 134],
            "textunits": [1469, 1885, 62, 1732, 1670, 128, 102,159,1920,201,207,483],
            "relationships": [300, 1283, 133],
            "claims": [2,5,7],
        }},
        {{
            "point": "The convenience of liquid products",
            "content": "Liquid products, such as liquid soap and certain types of shower gel, provide greater convenience in use. Many consumers like the way liquid products are used because they are easy to grasp and usually produce rich foam, with significant cleaning effects. Liquid products are also often seen as a relatively modern choice, and some users even see them as an upgrade to soap, although some consumers have doubts about the safety and effectiveness of their ingredients.",
            "entities": [1883, 1880, 971],
            "textunits": [1885, 1793, 773, 290, 739, 103, 287, 982],
            "relationships": [300, 1283, 133],
            "claims": [2,5,7],
        }},
        {{
            "point": "The experience and innovation of foam products",
            "content": "With the development of the market, foam products such as foam hand soap and foam shower gel have become the new favorites of consumers. They attract a large number of young consumers with their rich foam and pleasant user experience. Consumers' love for foam products usually stems from the sensory enjoyment they bring, while also having high expectations for cleaning effects. However, the gap between the marketing and actual effects of foam products has also raised doubts among some consumers, especially in terms of moisturizing and cleaning functions.",
            "entities": [497, 134],
            "textunits": [1885, 579, 488, 653, 673,684, 695, 900, 912, 954, 958, 983],
            "relationships": [300, 1283, 133],
            "claims": [2,5,7],
        }},
    ],
}}
where 1469, 1885, 1793, 579, and 488 represent the id (not the index) of the relevant data record.
END OF EXAMPLE


---Target response length and format---

{{
    "title": <User-provided question. Type: str>,
    "answer": "<Do you know the answer. True or False>",
    "summary": "<Summary of the response. Type: str>",
    "viewpoints": [
        {{
            "point": "<Opinion of the title. Type: str>",
            "content": "<Content of the opinion. Type: str>",
            "entities": <represent the id (not the index) of the entities data record. Type: list[num]>,
            "textunits": <represent the id (not the index) of the textunits data record. Type: list[num]>,
            "relationships": <represent the id (not the index) of the relationships data record. Type: list[num]>,
            "claims": <represent the id (not the index) of the claims data record. Type: list[num]>,
        }},
        {{
            "point": "<Opinion of the title. Type: str>",
            "content": "<Content of the opinion. Type: str>",
            "entities": <represent the id (not the index) of the entities data record. Type: list[num]>,
            "textunits": <represent the id (not the index) of the textunits data record. Type: list[num]>,
            "relationships": <represent the id (not the index) of the relationships data record. Type: list[num]>,
            "claims": <represent the id (not the index) of the claims data record. Type: list[num]>,
        }},
        {{
            "point": "<Opinion of the title. Type: str>",
            "content": "<Content of the opinion. Type: str>",
            "entities": <represent the id (not the index) of the entities data record. Type: list[num]>,
            "textunits": <represent the id (not the index) of the textunits data record. Type: list[num]>,
            "relationships": <represent the id (not the index) of the relationships data record. Type: list[num]>,
            "claims": <represent the id (not the index) of the claims data record. Type: list[num]>,
        }},
    ],
}}

The number of viewpoints is uncertain.

Do not include information where the supporting evidence for it is not provided.

Add sections and commentary to the response as appropriate for the length and format. Style the response in markdown.
"""

a = {
    "summary": "",
    "know_answer": "If you don't know the answer, just say so. Do not make anything up.",

    "data_references": "Points supported by data should list their data references as follows: 'This is an example sentence supported by multiple data references [Data: <dataset name> (record ids); <dataset name> (record ids)].'",


}
"""
### 香皂、液体和泡沫产品的观点分析

在个人护理产品的讨论中，香皂、液体和泡沫产品各自代表了不同的使用体验和消费者偏好。以下将对这三种产品进行详细分析，探讨它们的特点、使用感受以及消费者的看法。

#### 香皂的传统魅力

香皂作为一种传统的清洁产品，广泛用于洗澡和洗手。其使用习惯往往与长久以来的记忆相结合，很多用户在谈到香皂时会提到儿时的回忆和家人使用的品牌。这种情感联结使香皂在很多消费者心中占据特殊的位置。然而，现代消费者对香皂的看法也趋向于谨慎，尤其是对其保湿效果的质疑。某些消费者认为香皂可能会造成皮肤干燥或损害皮肤屏障，从而对其在日常护理中的有效性产生怀疑 [Data: Sources (1469, 1885, 62); Entities (307, 1883, 134)]。

#### 液体产品的便捷性

液体产品，如液体香皂和某些类型的洗浴露，在使用上提供了更大的便利。许多消费者喜欢液体产品的使用方式，因为它们容易掌握，且通常泡沫丰富，清洁效果显著。液体产品也常被视为相对更现代的选择，一些用户甚至将其视作对香皂的升级，尽管也有消费者对其成分的安全性和有效性表示疑虑 [Data: Sources (1885, 1793); Entities (1883, 1880, 971)]。

#### 泡沫产品的体验与创新

随着市场的发展，泡沫产品，如泡沫洗手液和泡沫沐浴露，成为了消费者新的宠儿。它们以其丰富的泡沫和愉悦的使用体验吸引了大量年轻消费者。消费者对泡沫产品的喜爱通常源于其带来的感官享受，同时对清洁效果抱有较高期望。然而，泡沫产品的营销和实际效果之间的差距也引发了一些消费者的怀疑，尤其是在保湿和清洁功能方面 [Data: Sources (1885, 579, 488); Entities (497, 134)]。

### 总结

综上所述，香皂、液体和泡沫产品各自拥有独特的市场定位和用户体验。香皂以其情感联结和传统价值继续占有一席之地，液体产品则因其便利性而受到现代消费者的青睐；而泡沫产品则依靠丰富的用户体验和新奇感占领了市场。尽管每种产品都有其优势，但它们的有效性和消费安全仍是消费者最为关注的议题。
"""
example = {
    "title": "Perspective analysis of soap, liquid and foam products",
    "summary": "In the discussion of personal care products, soaps, liquids, and foam products each represent different user experiences and consumer preferences. The following is a detailed analysis of these three products, exploring their characteristics, how they feel and how consumers perceive them.",
    "viewpoints": [
        {
            "opinion": "The traditional charm of soap",
            "content": "As a traditional cleaning product, soap is widely used for bathing and hand washing. Its usage habits are often combined with long-standing memories, and many users will mention childhood memories and the brands used by family members when talking about soap. This emotional connection makes soap occupy a special place in the hearts of many consumers. However, modern consumers' views on soap also tend to be cautious, especially about its moisturizing effect. Some consumers believe that soap may cause skin dryness or damage the skin barrier, casting doubt on its effectiveness in daily care.",
            "sources": [1469, 1885, 62],
        },
        {
            "opinion": "The convenience of liquid products",
            "content": "Liquid products, such as liquid soap and certain types of shower gel, provide greater convenience in use. Many consumers like the way liquid products are used because they are easy to grasp and usually produce rich foam, with significant cleaning effects. Liquid products are also often seen as a relatively modern choice, and some users even see them as an upgrade to soap, although some consumers have doubts about the safety and effectiveness of their ingredients.",
            "sources": [1885, 1793],
        },
        {
            "opinion": "The experience and innovation of foam products",
            "content": "With the development of the market, foam products such as foam hand soap and foam shower gel have become the new favorites of consumers. They attract a large number of young consumers with their rich foam and pleasant user experience. Consumers' love for foam products usually stems from the sensory enjoyment they bring, while also having high expectations for cleaning effects. However, the gap between the marketing and actual effects of foam products has also raised doubts among some consumers, especially in terms of moisturizing and cleaning functions.",
            "sources": [1885, 579, 488],
        },
    ],
}