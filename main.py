import argparse
from orchestrator.agentic_orchestrator import AgenticOrchestrator


def main():
    parser = argparse.ArgumentParser("Agentic MLOps System")
    
    parser.add_argument(
            "--mode",
            choices=["local", "cloud"],
            default="local",
            help="Execution mode"
        )
    parser.add_argument("--phase", required=True, 
                       choices=["baseline", "drift", "train", "deploy", "autonomous"],
                       help="Execution phase")
    parser.add_argument("--dataset", required=True, help="Dataset name")
    parser.add_argument("--cost", type=float, default=10.0, help="Cost budget")
    
    args = parser.parse_args()

    print(f"""
    🤖 AGENTIC MLOPS SYSTEM
    Phase:    {args.phase}
    Dataset:  {args.dataset}
    Budget:   ${args.cost}
    """)
    
    orchestrator = AgenticOrchestrator(
        phase=args.phase,
        dataset=args.dataset,
        cost=args.cost,
    )
    
    result = orchestrator.run()
    print(result)
    
    # if result["success"]:
    #     print(f"Execution completed: {result['summary']}")
    # else:
    #     print(f"Execution failed: {result['error']}")
    #     exit(1)


if __name__ == "__main__":
    main()
