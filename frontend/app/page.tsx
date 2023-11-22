import styles from './page.module.css';
import Homes from '../components/home/home';

export default function Home() {
	return (
		<main className={styles.main}>
			<Homes />
		</main>
	);
}