import math

# Noktaların tanımlanması
points = [(1, 2), (3, 4), (5, 6), (7, 8)]

# Öklid mesafesi hesaplama fonksiyonu
def euclideanDistance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)

# Mesafelerin hesaplanması
distances = []
for i in range(len(points)):
    for j in range(i + 1, len(points)):
        distance = euclideanDistance(points[i], points[j])
        distances.append((points[i], points[j], distance))

# Sonuçları yazdırma
for pair in distances:
    print(f"Noktalar: {pair[0]} ve {pair[1]} arasındaki mesafe: {pair[2]:.2f}")