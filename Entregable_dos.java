import java.util.*;
import java.util.Collections;

class Entregable_dos {

  public static void bucketSort(Student[] students) {
    final String[] courses = { "IB", "IG", "IN", "IS", "IT" };
    final int amountOfBuckets = courses.length;
    final int n = students.length;

    if (n == 0) return;

    LinkedList<LinkedList<Student>> buckets = new LinkedList<>(); //create buckets
    for (int i = 0; i < amountOfBuckets; i++) {
        buckets.add(new LinkedList<>()); //fill bucketlist with buckets
    }

    for (int i = 0; i < courses.length; i++) {
        for (Student student : students) {
            if (student.getClassNumber().startsWith(courses[i])) {
                buckets.get(i).add(student);
            }
        }
    }

    for (int i = 0; i < amountOfBuckets; i++) {
        LinkedList<Student> studentLinkedList = buckets.get(i);
        Student[] s = studentLinkedList.toArray(new Student[studentLinkedList.size()]);
        insertionSortByClass(s);
        studentLinkedList = new LinkedList<>(Arrays.asList(s));
        buckets.set(i, studentLinkedList);
    }

    LinkedList<Student> result = new LinkedList<>();
    for (LinkedList<Student> bucket : buckets) {
        result.addAll(bucket);
    }

    for (int i = 0; i < result.size(); i++) {
        students[i] = result.get(i);
    }
}
}
