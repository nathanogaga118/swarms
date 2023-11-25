from swarms.structs import Flow
from swarms.models.gpt4_vision_api import GPT4VisionAPI


llm = GPT4VisionAPI()

task = "Analyze this image of an assembly line and identify any issues such as misaligned parts, defects, or deviations from the standard assembly process. IF there is anything unsafe in the image, explain why it is unsafe and how it could be improved."
img = "assembly_line.jpg"

## Initialize the workflow
flow = Flow(
    llm=llm,
    max_loops=1,
    dashboard=True,
)

flow.run(task=task, img=img)
