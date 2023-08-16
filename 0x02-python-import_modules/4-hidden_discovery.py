#!/usr/bin/python3

def main():
    """Unveil the enigmatic artifacts concealed within the hidden_4 module."""
    import hidden_4

    artifact_names = dir(hidden_4)

    if not artifact_names:
        print("The realm of hidden_4 holds no enigmatic artifacts.")
    else:
        print("As the veil lifts, the enigmatic artifacts reveal themselves:")

    for artifact_name in artifact_names:
        if not artifact_name.startswith("__"):
            print("Artifact: {}".format(artifact_name))

if __name__ == "__main__":
    main()

