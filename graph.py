from langgraph.graph import StateGraph, END
from state import AgentState
from tools import web_search, fetch_page, summarize

MAX_STEPS = 6


def search_node(state: AgentState):
    print("\nSearching the web...")

    results = web_search(state["question"])

    print(f"Search results found: {len(results)}")

    state["search_results"] = results
    state["steps"] += 1
    return state


def fetch_node(state: AgentState):
    print("\nFetching webpages...")

    pages = []
    sources = []

    for result in state["search_results"][:3]:
        text = fetch_page(result["url"])

        if text:
            pages.append({
                "title": result["title"],
                "text": text
            })
            sources.append(result["url"])
            print("Fetched:", result["title"])
        else:
            print("Failed:", result["title"])

    state["pages"] = pages
    state["sources"] = sources
    state["steps"] += 1

    return state


def summary_node(state: AgentState):
    print("\nSummarizing information...")

    if not state["pages"]:
        state["summary"] = "No reliable information could be fetched."
        state["steps"] += 1
        return state

    combined = ""

    for page in state["pages"]:
        combined += page["text"] + "\n\n"

    state["summary"] = summarize(combined, state["question"])
    state["steps"] += 1

    return state


def router(state: AgentState):

    if state["steps"] >= MAX_STEPS:
        print("Step limit reached.")
        return END

    if len(state["search_results"]) == 0:
        state["summary"] = "No search results found."
        return END

    if len(state["pages"]) == 0:
        return "fetch"

    if state["summary"] == "":
        return "summary"

    return END


builder = StateGraph(AgentState)

builder.add_node("search", search_node)
builder.add_node("fetch", fetch_node)
builder.add_node("summary", summary_node)

builder.set_entry_point("search")

builder.add_conditional_edges(
    "search",
    router,
    {
        "fetch": "fetch",
        END: END
    }
)

builder.add_conditional_edges(
    "fetch",
    router,
    {
        "summary": "summary",
        END: END
    }
)

builder.add_edge("summary", END)

graph = builder.compile()