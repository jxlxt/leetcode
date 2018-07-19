package edu.ucsc;

import java.util.HashMap;
import java.util.List;
import java.util.Map;

/**
// Employee info
class Employee {
    // It's the unique id of each node;
    // unique id of this employee
    public int id;
    // the importance value of this employee
    public int importance;
    // the id of direct subordinates
    public List<Integer> subordinates;
};
*/

/**
 * Leetcode Number: 690
 * Leetcode Problem Name: Employee Importance
 * Data:05/18/2018,4:41pm
 * Writer: Xiaotong Li
 */
public class getImportance {
    public int getImportance(List<Employee> employees, int id){
        Map<Integer, Employee> map = new HashMap<Integer, Employee>();
        for (Employee employee : employees) {
            map.put(employee.id, employee);
        }
        return getImportanceHelper(map, id);
    }

    private int getImportanceHelper(Map<Integer, Employee> map, int rootId) {
        Employee root = map.get(rootId);
        int total = root.importance;
        for (int subordinate : root.subordinates) {
            total += getImportanceHelper(map, subordinate);
        }
        return total;
    }
}
