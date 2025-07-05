
from utils.model_loader import ModelLoader
from prompt_library.prompt import SYSTEM_PROMPT
from langgraph.graph import StateGraph, MessagesState, END, START
from langgraph.prebuilt import ToolNode, tools_condition
from tools.weather_info_tool import WeatherInfoTool
from tools.place_search_tool import PlaceSearchTool
from tools.expense_calculator_tool import CalculatorTool
from tools.currency_conversion_tool import CurrencyConverterTool





class GraphBuilder():
    def __init__(self,graph):
        self.tools=[



        ]
        self.system_prompt=SYSTEM_PROMPT


    def agent_function(self,state: MessagesState):
        """Main Afent function that processes user messages and invokes the LLM with tools."""
        user_quesion=state["messages"]
        input_question= [self.system_prompt] + user_quesion
        response=self.llm_with_tools.invoke(input_question)
        return {"messages":[response]}


    def build_graph(self):
        graph_builder=StateGraph(MessagesState)
        graph_builder.add_node("agent", self.agent_function)
        graph_builder.add_node("tools", ToolNode(tools=self.tools))
        graph_builder.add_edge(START,"agent")
        graph_builder.add_conditional_edges("agent",tools_condition)
        graph_builder.add_edge("tools","agent")
        graph_builder.add_edge("agent",END)
        self.graph = graph_builder.compile()
        return self.graph
       

    def __call__(self, *args, **kwds):
        return self.build_graph()

