import mido

tab = []
with mido.MidiFile("output.mid") as inport:
    for msg in inport:
        print(msg)
        tab += str(msg).split(' ')

notes = [[], []]
for i in tab:
    if i[0:5] == 'note=':
        notes[0].append(i.split("=")[1])
    elif i[0:4] == 'time':
        notes[1].append(i.split("=")[1])

notes[1] = notes[1][2:-1]
notes[0] = notes[0][1::2]
notes[1] = notes[1][1::2]
print(notes[0], notes[1])

