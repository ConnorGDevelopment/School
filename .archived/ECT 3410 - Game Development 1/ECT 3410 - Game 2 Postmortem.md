# ECT 3410 - Game 2 Postmortem

By Rev Guarino

## What went right?

I think we did a really great job of scoping our project. We had a clear direction of what we were going to make and what we were not going to make. Additionally, the objectives we had scoped were all solid additions because they were based on elements we thought our first game needed or things we wanted to add.

## What went wrong?

The XR Device Simulator is the work of the devil. I rely on the XR Device Simulator a lot because my Visual Snow Syndrome gives me really bad vertigo and nausea when I use VR. I can adjust if I stay in VR for a period, but during development it is headset on and off repeatedly. It took a week or more to get it functioning correctly in our project and then there were several bugs or oddities that cropped up that double the development time on certain features.

The biggest thing I think went wrong was my part, the Rogue System. I had originally designed it to use a Scriptable Object as the base unit with a Mono Behaviour as a manager, and this is what I handed off to Eric for him to develop with. Then while he worked on his features, I made revisions to the system to make it easier to use. I thought this would be fine because all of my work would be a commit that would overwrite the original version. But it was not because I had actually moved everything down a hierarchy, my base unit was a Dictionary that was wrapped by a Scriptable Object and then manage by a Mono Behaviour. This meant that when I pushed my code, there were a bunch of interactions in the code that weren't supported like using operators with Stat Blocks. So to preserve the front side code and what would actually get played, it had to be left out of the final submission.

Also, I think our group was to some degree dysfunctional. There was me and Eric that were knee deep in the project and motivated. But we didn't do a great job of setting out work for Britney and Nick, and they weren't really invested in the project at all. So it was kind of left up in the air what contributions they wanted to make.

## What would you do differently if you could start over again?

First, I think it would have helped if we had designed for a 3D shooter game that could be played in VR, to make testing much easier. I wanted to be a champ and a team player so I didn't express how much off a setback solo-VR was, and that came back to bite me.

I think planning out our feature additions down to the branches and commits we'll make would have helped immensely. Looking back, of course my Rogue System commit was going to be a problem. I changed the mechanisms it was using to interact and it was a system that was going to be woven throughout all of the code. It didn't matter that the commit itself was going to be self-contained. If we had planned out when the feature was going to be merged into main or the changes I would make in my revisions, we wouldn't have put ourselves in a position where a bunch of stuff was built off a flawed system and having the revised version being a breaking a change.

In terms of group, I'm unsure of what next steps would be. I could say like find group members that are more experienced in the areas they are going to contribute but that's kind of a cop-out and avoids better delegation. I think if we had spent time rallying the team together and making sure everyone is excited and involved, then we would have been better able to gauge everyone's skill level and potential.
