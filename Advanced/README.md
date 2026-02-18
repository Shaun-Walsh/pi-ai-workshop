# Advanced Projects - Extension Activities

**For fast finishers, extended workshops, and homework challenges**

---

## 🎯 Overview

These advanced projects are **optional extensions** to the main workshop curriculum (Scripts 1-5). They introduce new concepts and provide fun, engaging challenges for students who:

- Finish the main curriculum early
- Want additional practice
- Are interested in game development
- Need homework/follow-up activities

**Key Difference:** These projects introduce the **joystick** (5-way control) which wasn't covered in the main curriculum.

---

## 📁 Projects Included

### 1. **[Joystick Basics](advanced_1_joystick_basics.py)** - Event-Driven Programming
**Difficulty:** ⭐⭐ Easy
**Duration:** 20-30 minutes
**Prerequisites:** Scripts 1-2

**What students learn:**
- Event-driven programming (responding to user input)
- The Sense HAT joystick (up, down, left, right, middle)
- Event loops and event objects
- Real-time interactive programs
- Statistics and data tracking

**What it does:**
- Press joystick in any direction
- LED matrix lights up with corresponding color
- Tracks how many times each direction was pressed
- Shows statistics when exiting

**Why this is useful:**
- All interactive software uses event-driven programming
- Teaches fundamental concept for game development
- Prepares for more complex interactive projects

---

### 2. **[Digital Dice](advanced_2_digital_dice.py)** - Shake to Roll!
**Difficulty:** ⭐⭐⭐ Medium
**Duration:** 30-45 minutes
**Prerequisites:** Scripts 2-3 (sensors + accelerometer)

**What students learn:**
- Combining multiple components (accelerometer + LED patterns)
- Creating custom LED patterns (2D lists)
- Random number generation
- Shake/movement detection
- Statistics and probability

**What it does:**
- Shake the Raspberry Pi (like shaking dice)
- Shows rolling animation
- Displays dice face (1-6 dots) on LED matrix
- Tracks rolling statistics

**Why this is useful:**
- Combines multiple skills from main curriculum
- Introduces custom visual patterns
- Practical application of randomness
- Fun and immediately rewarding!

**Math connection:**
- Probability (each number should appear ~16.67% of time)
- Statistical analysis (fair vs loaded dice)
- Averages and distributions

---

### 3. **[Reaction Game](advanced_3_reaction_game.py)** - Test Your Reflexes!
**Difficulty:** ⭐⭐⭐ Medium
**Duration:** 30-45 minutes
**Prerequisites:** Script 1 + Advanced 1 (joystick basics)

**What students learn:**
- Timing and performance measurement
- Combining randomness with user input
- Game loops and state management
- User interface design (feedback, prompts)
- Performance tracking and analysis

**What it does:**
- Wait for random color to appear on LED matrix
- Press matching joystick direction as fast as possible
- Measures reaction time in milliseconds
- Provides performance rating (Elite, Excellent, Good, etc.)
- Tracks statistics across multiple rounds

**Why this is useful:**
- Complete game with scoring system
- Real-world application (testing reflexes)
- Engaging and competitive
- Teaches timing/performance measurement

**Science connection:**
- Human reaction time (average: 200-300ms)
- Factors affecting performance (practice, fatigue, age)
- Experimental design (hypothesis testing)

---

## 🎓 When to Use These Projects

### During Main Workshop:
- **Fast finishers** who complete Scripts 1-5 early
- **Break-out sessions** for advanced students
- **Demonstration** of what's possible with the Pi

### Extended Workshops:
- **Day 2** of a multi-day workshop
- **Follow-up session** after completing main curriculum
- **Project time** for students to choose what interests them

### Homework/Independent Learning:
- **Take-home challenges** for motivated students
- **Optional assignments** for extra credit
- **Portfolio pieces** to showcase skills

### Special Sessions:
- **Game development workshop** (all 3 projects)
- **Probability & statistics** (focus on Digital Dice)
- **User interface design** (focus on Reaction Game)

---

## 📊 Difficulty Progression

```
Main Curriculum (Scripts 1-5)
    ↓
Advanced 1: Joystick Basics ⭐⭐
    ↓ (Introduces new input method)
Advanced 2: Digital Dice ⭐⭐⭐
    ↓ (Combines accelerometer + LED patterns)
Advanced 3: Reaction Game ⭐⭐⭐
    ↓ (Full game with scoring + timing)
```

**Recommended order:**
1. Complete main curriculum first (Scripts 1-5)
2. Start with Advanced 1 (introduces joystick)
3. Choose Advanced 2 OR 3 based on interest
4. Complete remaining project if time allows

---

## 🎯 Learning Objectives

### Technical Skills:
- ✅ Event-driven programming paradigm
- ✅ Joystick input handling
- ✅ Custom LED pattern creation (2D lists)
- ✅ Random number generation
- ✅ Timing and performance measurement
- ✅ Shake detection algorithms
- ✅ State management
- ✅ User interface feedback design

### Programming Concepts:
- ✅ Event loops
- ✅ Event objects (properties: direction, action)
- ✅ Dictionaries for mapping
- ✅ 2D lists (grids/matrices)
- ✅ Statistical analysis
- ✅ Game loop architecture

### Math & Science:
- ✅ Probability and statistics
- ✅ Acceleration and magnitude calculation
- ✅ Reaction time measurement
- ✅ Data visualization (bar charts)
- ✅ Averages and percentages

---

## 👥 Teaching Strategies

### For Mixed-Ability Groups:
- **Advanced students:** Work independently on these projects
- **Struggling students:** Continue with main curriculum challenges
- **Peer teaching:** Advanced students help others when done

### For Competitive Students:
- **Leaderboards:** Display best reaction times or most accurate dice statistics
- **Tournaments:** Organize competitions between students
- **Challenges:** "Can you beat the teacher's time?"

### For Creative Students:
- **Customization:** Encourage modifying colors, patterns, rules
- **Extensions:** Point them to the challenge sections in each script
- **Invention:** "Create your own game using these concepts"

---

## 📋 Assessment Ideas

### Formative (During Activity):
- Can student explain what an "event" is?
- Can they modify colors/timing independently?
- Do they understand why random.randint() produces different results?

### Summative (End of Project):
1. **Demonstration:** Show working project to class
2. **Modification:** Change one feature (color, speed, rules)
3. **Explanation:** Describe one new concept learned
4. **Extension:** Complete at least one challenge from script

### Portfolio Assessment:
- Screenshot/video of working project
- Written reflection on what they learned
- Code with custom modifications
- Statistical analysis (for Dice or Reaction Game)

---

## 🔧 Setup Requirements

### Hardware:
- Same as main curriculum (Pi + Sense HAT)
- **No camera required** for these projects
- Works perfectly in headless mode via SSH

### Software:
- Same as main curriculum (sense-hat library)
- No additional installations needed

### Time:
- Each project: 30-45 minutes
- All three projects: 2-3 hours total

---

## 🐛 Common Issues & Solutions

### Joystick not responding:
```bash
# Check Sense HAT connection
sudo reboot

# Verify with test
python3 -c "from sense_hat import SenseHat; s = SenseHat(); print(s.stick.wait_for_event())"
```

### Dice too sensitive/not sensitive enough:
- Adjust `shake_threshold` in advanced_2_digital_dice.py
- Default: 1.5 (try 1.2 for more sensitive, 2.0 for less)

### Reaction game shows negative times:
- System clock issue (rare)
- Run: `sudo ntpd -qg` to sync time
- Restart script

---

## 💡 Extension Ideas

### For Students Who Want More:

1. **Combine Projects:**
   - Use joystick to switch between Dice and Reaction Game
   - Create a "game menu" system

2. **Add Complexity:**
   - Multi-player modes
   - High score saving (to file)
   - Different difficulty levels

3. **Create New Games:**
   - Memory game (Simon Says)
   - Snake game (joystick controls)
   - Maze game (navigate LED matrix)
   - Tic-tac-toe (two players)

4. **Add Features:**
   - Sound effects (pygame.mixer)
   - Network multiplayer (sockets)
   - Web dashboard (Flask)

---

## 📚 Resources

### For Students:
- [Sense HAT Joystick API](https://pythonhosted.org/sense-hat/api/#joystick)
- [Python random module](https://docs.python.org/3/library/random.html)
- [Event-driven programming](https://en.wikipedia.org/wiki/Event-driven_programming)

### For Teachers:
- Challenge solutions (available in script comments)
- Extension project ideas (see script documentation)
- Assessment rubrics (in main WORKSHOP_GUIDE.md)

---

## 🎮 Project Comparison

| Feature | Joystick Basics | Digital Dice | Reaction Game |
|---------|----------------|--------------|---------------|
| **Input** | Joystick only | Shake (accel) | Joystick only |
| **Output** | Solid colors | Dice patterns | Color flashes |
| **Complexity** | Low | Medium | Medium |
| **Duration** | 20-30 min | 30-45 min | 30-45 min |
| **New Concepts** | Events | 2D lists, random | Timing, scoring |
| **Fun Factor** | 😊 Interactive | 🎲 Game-like | 🏆 Competitive |
| **Best For** | Learning basics | Math/stats | Quick reflexes |

---

## ✅ Success Criteria

Students have successfully completed advanced projects when they can:

- ✅ Explain what "event-driven programming" means
- ✅ Demonstrate joystick controlling LED matrix
- ✅ Describe how shake detection works (accelerometer magnitude)
- ✅ Create custom dice patterns using 2D lists
- ✅ Understand randomness and probability
- ✅ Measure and compare reaction times
- ✅ Modify one project independently

---

## 🎉 Showcase Ideas

**End-of-Workshop Demonstrations:**
1. **Dice Rolling Championship:** Who can roll the most 6s in 20 rolls?
2. **Reaction Time Olympics:** Class leaderboard of fastest times
3. **Custom Creations:** Students show their modified versions
4. **Peer Teaching:** Advanced students teach one concept to class

---

**These projects are designed to be FUN, EDUCATIONAL, and ACHIEVABLE!**

**Let students explore, experiment, and express creativity! 🚀**

---

*Last Updated: February 2026*
