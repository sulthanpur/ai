def monkey_banana_problem():
    # Initial state
    monkey_location = "Far"         # Monkey is far from chair
    chair_position = "NotUnder"     # Chair is not under banana
    monkey_on_chair = False         # Monkey is not on the chair
    has_banana = False              # Monkey doesn't have the banana

    print("Initial State:")
    print("Monkey Location:", monkey_location)
    print("Chair Position:", chair_position)
    print("Monkey On Chair:", monkey_on_chair)
    print("Has Banana:", has_banana)
    print()

    steps = []

    # Step 1: Move to chair
    if monkey_location != "Near":
        monkey_location = "Near"
        steps.append("Monkey moves near the chair.")

    # Step 2: Push chair under banana
    if chair_position != "Under":
        chair_position = "Under"
        steps.append("Monkey pushes the chair under the banana.")

    # Step 3: Climb the chair
    if not monkey_on_chair:
        monkey_on_chair = True
        steps.append("Monkey climbs on the chair.")

    # Step 4: Grasp banana
    if monkey_on_chair and chair_position == "Under" and monkey_location == "Near":
        has_banana = True
        steps.append("Monkey grasps the banana.")

    # Print steps
    print("Steps to reach the banana:\n")
    for step in steps:
        print(step)

    # Final state
    print("\nFinal State:")
    print("Monkey Location:", monkey_location)
    print("Chair Position:", chair_position)
    print("Monkey On Chair:", monkey_on_chair)
    print("Has Banana:", has_banana)

    if has_banana:
        print("\n✅ Success: Monkey got the banana!")
    else:
        print("\n❌ Failure: Monkey didn't get the banana.")

# Run the program
monkey_banana_problem()
