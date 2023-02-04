def lines(filename):
    f = open(filename + ".txt", "r")
    text = f.read()
    f.close()
    return text.splitlines()

def convert_time(t):
    times = t.split(":")
    minutes = int(times[0])
    hours = str(minutes//60).zfill(2)
    minutes = str(minutes%60).zfill(2)
    return hours + ":" + minutes + ":" + times[1] + ",500"

def make_srt(n, t1, t2, line):
    data = str(n+1) + "\n"

    ct1 = convert_time(t1)
    list_t1 = ct1[:8].split(":")
    int_t1 = int(list_t1[0])*3600 + int(list_t1[1])*60 + int(list_t1[2])

    ct2 = convert_time(t2)
    list_t2 = ct2[:8].split(":")
    int_t2 = int(list_t2[0])*3600 + int(list_t2[1])*60 + int(list_t2[2])

    dif = int_t2 - int_t1

    if(dif > 8):
        int_t1 += 8
        hours = int_t1//3600
        int_t1 -= hours*3600
        minutes = int_t1//60
        int_t1 -= minutes*60
        ct2 = str(hours).zfill(2) + ":" + str(minutes).zfill(2) + ":" + str(int_t1).zfill(2) + ",500"
    data += ct1 + " --> " + ct2 + "\n"
    data += line + "\n"
    data += "\n"
    return data

#main

fn = input("enter a the filename (without extension) of a .txt file with subtitles in YT format: ")

subs = lines(fn)
times = lines("mirrorpt")



#creates file
f = open(fn + ".srt", "x")
f.close()

f = open(fn + ".srt", "a")

for i in range(0, len(subs) - 3, 2):
    t1 = times[i]
    line = subs[i+1]
    t2 = times[i+2]

    srt_write = make_srt(i//2, t1, t2, line)
    f.write(srt_write)



