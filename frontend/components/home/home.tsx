import styles from './home.module.css';

export default function About() {
	return (
        <section className={styles.container}>
            <div className={styles.title}>
                <h1>Health and Fitness Tracker</h1>
            </div>
            <div className={styles.body}>
                <p>
                    Fitness and Health Tracker is a Python-based application designed to 
                    help users monitor and analyze their physical activities, 
                    dietary habits, and other health metrics. The project leverages the 
                    Google Sheets API for easy data input and manipulation.
                </p>
            </div>
        </section>
    );
}