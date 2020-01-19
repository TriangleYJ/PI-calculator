# pi calculator
# In this code, any constant related to PI doesn't used.


# collision velocity exchange formula
# input : front object array, back object array
# output : velocity front, velocity back

def collision(front, back):
    m1 = front[0]
    m2 = back[0]
    v1 = front[1]
    v2 = back[1]

    v1prime = ((m1 - m2) * v1 + 2 * m2 * v2) / (m1 + m2)
    v2prime = ((m2 - m1) * v2 + 2 * m1 * v1) / (m1 + m2)

    return v1prime, v2prime


# See this. The most unexpected answer to a counting puzzle. https://www.youtube.com/watch?v=HEfHFsfGXjs
# input : the length of pi under decimal point.
# output : pi sequence until input number.
# Big-O notation : O(2^n)

def printPI_collision(length):
    # constants related to collision calculation
    # [mass, velocity]
    a = [1, 0]
    b = [pow(10, 2 * length), -1]
    count = 0

    # if a.velocity is bigger than b.velocity (ex. a = 0, b = -10 [<-] ), calculate collision, count
    # if a.velocity is smaller than 0, just change its velocity to positive, and count
    # until a.velocity is smaller than b.velocity (ex. a = 10[->], b = 20 [-->]), calculate #1

    while a[1] >= b[1]:
        c = collision(a, b)
        a[1] = c[0]
        b[1] = c[1]
        count += 1

        if a[1] < 0:
            a[1] = -a[1]
            count += 1

    print(count)


printPI_collision(7)
