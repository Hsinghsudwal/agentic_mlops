import argparse
from orchestrator.agentic_orchestrator import AgenticOrchestrator


def main():
    parser = argparse.ArgumentParser(
        description="Agentic MLOps Orchestrator",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python main.py --goal baseline --dataset wine --dataset-path ./data/wine.csv
  python main.py --goal ml_train --dataset wine --dataset-path ./data/wine.csv --prefix init --extra deploy --env local
  python main.py --goal deploy --dataset wine --dataset-path ./data/wine.csv --prefix prod
        """
    )
    parser.add_argument(
        "--goal",
        required=True,
        choices=["baseline", "ml_train", "serve", "deploy", "monitor", "heal"],
        help="Goal/Intent to execute"
    )
    parser.add_argument(
        "--dataset",
        required=True,
        help="Dataset name"
    )
    
    parser.add_argument(
        "--dataset-path",
        required=True,
        help="Path to dataset"
    )
    parser.add_argument(
        "--prefix",
        default="init",
        help="Artifact prefix (init, replay, hotfix, shadow, prod)"
    )
    

    args = parser.parse_args()
    
    orchestrator = AgenticOrchestrator(
        intent=args.goal,
        dataset=args.dataset,
        dataset_path=args.dataset_path,
        prefix=args.prefix
    )
    
    result = orchestrator.run()
    
    if result["success"]:
        print(f"Execution completed: {result['summary']}")
    else:
        print(f"Execution failed: {result['error']}")
        exit(1)


if __name__ == "__main__":
    main()